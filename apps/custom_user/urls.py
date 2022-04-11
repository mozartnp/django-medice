from django.urls import path 

from custom_user.views import homepageview, LogIn, SingUp

urlpatterns = [
    path('', homepageview, name='homepage'),
    path('login', LogIn.as_view(), name= 'login'),
    path('singup', SingUp.as_view(), name='singup'),
]