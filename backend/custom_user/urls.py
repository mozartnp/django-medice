from django.urls import path

from .views import AuthLogin, AuthSignup

app_name = 'custom_user'

urlpatterns = [
    path('login', AuthLogin.as_view(), name='login'),
    path('signup', AuthSignup.as_view(), name='signup'),
]
