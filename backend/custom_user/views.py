from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from backend.custom_user.forms import SignupForm
from backend.custom_user.models import CustomUser


# TODO a CBV aqui seria createview, uma vez que vou criar uma item no model?
# TODO Como eu testo um CBV de forma certa, o que preciso olhar?
# TODO ter mais de um success_url
class AuthSignup(CreateView):
    model = CustomUser
    form_class = SignupForm
    template_name = "custom_user/signup.html"
    success_url = "homepage"  # FIXME mudar


class AuthLogin(LoginView):
    template_name = "custom_user/login.html"
