from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from backend.custom_user.forms import SignupForm
from backend.custom_user.models import User


# TODO a CBV aqui seria createview, uma vez que vou criar uma item no model?
# TODO Como eu testo um CBV de forma certa, o que preciso olhar?
# TODO ter mais de um success_url
class AuthSignup(CreateView):
    model = User
    template_name = "custom_user/signup.html"
    form_class = SignupForm

    def get_success_url(self):
        '''
        Define o redirect dependendo do tipo de usuário.
        '''
        if self.object.user_type == 'MEDI':
            return reverse_lazy('core:index')

        if self.object.user_type == 'PACI':
            return reverse_lazy('custom_user:signup')

        return reverse_lazy('custom_user:login')


class AuthLogin(LoginView):
    template_name = 'custom_user/login.html'

    def get_success_url(self):
        '''
        Define o redirect dependendo do tipo de usuário.
        '''
        if self.request.user.user_type == 'MEDI':
            return reverse_lazy('core:index')

        if self.request.user.user_type == 'PACI':
            return reverse_lazy('custom_user:signup')

        return reverse_lazy('custom_user:login')
