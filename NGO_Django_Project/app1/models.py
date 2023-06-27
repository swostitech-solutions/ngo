from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.

#create catagory model

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    #image showing method
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:30%;"/>'.format(self.image))

# Create Post Model
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content= models.TextField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')
    current_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:30%;"/>'.format(self.image))


#contact model

class Contact_model(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=70)
    address=models.CharField(max_length=70)
    message=models.TextField(max_length=200)

# payment tracking

class donation_payment_model(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    order_id=models.CharField(max_length=100,blank=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True)
    paid= models.BooleanField(default=False)



