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
    success_url = reverse_lazy('core:index')
