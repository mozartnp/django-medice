from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from backend.accounts.forms import SignupForm
from backend.accounts.models import User


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
            return reverse_lazy('core:index')

        if self.object.user_type == 'PACI':
            return reverse_lazy('accounts:signup')

        return reverse_lazy('accounts:login')


class AuthLogin(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        '''
        Define o redirect dependendo do tipo de usuário.
        '''
        if self.request.user.user_type == 'MEDI':
            return reverse_lazy('core:index')

        if self.request.user.user_type == 'PACI':
            return reverse_lazy('accounts:signup')

        return reverse_lazy('accounts:login')
