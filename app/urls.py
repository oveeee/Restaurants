
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm,SendEmail,ConfirmPassword,PasswordChangeForm
from django.conf import settings
from django.conf.urls.static import static
from customer.views import *

urlpatterns = [
    
    path('', views.home),
    path('profile/', views.profile, name='profile'),
    path('Testmonial/',views.Testmonial,name='Testmonial'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('ourservice/', views.ourservice, name='ourservice'),
    path('profile', views.order, name='order'),
    path('address',views.address, name='address'),
    #path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.
         as_view(template_name='login.html', authentication_form=LoginForm),name='login'),


    #path('singup/', views.singup, name='singup'),
    path('singup/', views.RegistrationView.as_view(), name="singup"),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),


    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',form_class=SendEmail),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=ConfirmPassword,success_url ='/accounts/login'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


    
    
    path('changepass/', auth_views.PasswordChangeView.as_view(template_name='changepass.html',form_class=PasswordChangeForm,success_url='/'), name='changepass'),
    #path('product-detail/', views.product_detail, name='product-detail'),
    #path('customer/',customer_views, name='customer'),
    #path('customers/',customers_views, name='customers'),
    path('test/',views.test,name='test'),
    
]