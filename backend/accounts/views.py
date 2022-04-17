from django.contrib.auth.views import (
    LoginView,
    PasswordResetConfirmView,
    PasswordResetView
)
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView

from backend.accounts.forms import SignupForm
from backend.accounts.models import User

from .tokens import account_activation_token


def send_mail_to_user(request, user):
    current_site = get_current_site(request)
    use_https = request.is_secure()
    subject = 'Ative sua conta.'
    message = render_to_string('email/account_activation_email.html', {
        'user': user,
        'protocol': 'https' if use_https else 'http',
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    user.email_user(subject, message)


# TODO a CBV aqui seria createview, uma vez que vou criar uma item no model?
# TODO Como eu testo um CBV de forma certa, o que preciso olhar?
# TODO ter mais de um success_url
class AuthSignup(CreateView):
    model = User
    template_name = "accounts/signup.html"
    form_class = SignupForm

    def get_success_url(self):
        '''
        Define o redirect dependendo do tipo de usuário.
        '''
        if self.object.user_type == 'MEDI':
            return reverse_lazy('patient:doctor_list')

        if self.object.user_type == 'PACI':
            return reverse_lazy('patient:patient_list')

        return reverse_lazy('core:index')

    def form_valid(self, form):
        self.object = form.save()
        send_mail_to_user(request=self.request, user=self.object)
        return super().form_valid(form)


class AuthLogin(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        '''
        Define o redirect dependendo do tipo de usuário.
        '''
        if self.request.user.user_type == 'MEDI':
            return reverse_lazy('patient:doctor_list')

        if self.request.user.user_type == 'PACI':
            return reverse_lazy('patient:patient_list')

        return reverse_lazy('core:index')


# Requer
# registration/password_reset_email.html
# registration/password_reset_subject.txt
class MyPasswordReset(PasswordResetView):
    ...


class MyPasswordResetConfirm(PasswordResetConfirmView):
    ...
