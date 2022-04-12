from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import AuthLogin, AuthSignup

app_name = 'custom_user'

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='custom_user/login.html'), name='login'),
    path('login/', AuthLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', AuthSignup.as_view(), name='signup'),
]
