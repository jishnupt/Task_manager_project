from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homepage',homepage,name='homepage'),
    path('UserRegister',RegisterUser,name='UserRegister'),
    path('Login_page',Login_page,name='Login_page'),
    path('AdminRegist',AdminRegist,name='AdminRegist'),
    path('user_dashbord',user_dashbord,name='user_dashbord'),
    path('Logout_page',Logout_page,name='Logout_page'),
    path('TaskAdding',TaskAdding,name='TaskAdding')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)