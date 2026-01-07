from django.urls import path
from .views import *

urlpatterns = [
    path('homepage',homepage),
    path('UserRegister',RegisterUser,name='UserRegister'),
    path('Login_page',Login_page,name='Login_page')
]