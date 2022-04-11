from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

from custom_user.forms import SingUpForm
from custom_user.models import CustomUser

#TODO não faz sentido isso ser um CBV?
def homepageview(request):
    return render(request, 'website/homepage.html')

#TODO a CBV aqui seria createview, uma vez que vou criar uma item no model?
#TODO Como eu testo um CBV de forma certa, o que preciso olhar?
#TODO ter mais de um success_url
class SingUp(CreateView):
    model = CustomUser 
    form_class = SingUpForm
    template_name = "website/singup.html"
    success_url = "homepage"#FIXME mudar
    
class LogIn(LoginView):
    template_name = "website/login.html"