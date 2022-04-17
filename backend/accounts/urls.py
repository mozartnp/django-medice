from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from backend.accounts import views as v

# Se usar app_name vai dar erro de redirect em PasswordResetView.
# app_name = 'accounts'


urlpatterns = [
    # path('login/', v.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('login/', v.AuthLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', v.AuthSignup.as_view(), name='signup'),
    path(
        'password_reset/',
        v.MyPasswordReset.as_view(),
        name='password_reset'
    ),
    path(
        'reset/<uidb64>/<token>/',
        v.MyPasswordResetConfirm.as_view(),
        name='password_reset_confirm'
    ),
]
