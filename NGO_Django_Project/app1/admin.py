from django.contrib import admin
from .models import Category
from .models import Post,Contact_model,donation_payment_model

# Register your models here.

#configrution of catagory admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id','image_tag','title','description','url','add_date')
    search_fields = ('title',)
    list_per_page = 5



class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id','image_tag','title','url','cat','current_date')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5

    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce.min.js', 'app1/js/script.js')


class Contact_model_Admin(admin.ModelAdmin):
    list_display = ('name','email','address','message')





class donation_payment_model_Admin(admin.ModelAdmin):
    list_display = ('name','amount','order_id','razorpay_payment_id','paid')

admin.site.register(Contact_model,Contact_model_Admin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(donation_payment_model,donation_payment_model_Admin)


