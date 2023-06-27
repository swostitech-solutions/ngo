from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import home,Post,Category

urlpatterns = [
    path('',views.home),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('about/',views.About, name='about'),
    path('contact/',views.contact, name='contact'),
    path('payment/',views.payment_view, name='payment'),
    path('payment-status/',views.payment_status_view, name='payment-status'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('signup/',views.user_signup, name='signup'),
    # path('post/<slug:url>',views.post),
    path('posts/',views.post_view, name='posts'),
    path('catpost/<slug:url>',views.cat_post_view, name='cat_post_view'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

