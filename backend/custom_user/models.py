from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


def user_type():
    '''
    Tipos de escolha do usuario 
    '''
    choice = [
        ('MEDI', _('Médico')),
        ('PACI', _('Paciente')),
    ]  
    return choice

class CustomUserManager(BaseUserManager):
    '''
    Class que criar o usuario, necessario para criação de um usuario customizado.
    '''
    def create_user(self, email, user_type, password=None):
        if not email:
            raise ValueError("É obrigatório o e-mail.")
        if not user_type:
            raise ValueError("É necessario definir se é paciente ou médico.")

        user = self.model(
            email = self.normalize_email(email),
            user_type = user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_type, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            user_type = user_type,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

#TODO Salvar usuario customizado com outra forma de id, criptografado?
#TODO Porque quando eu crio um superuser, ele vai para a tabela auth_user, e não para CustomUser?
#TODO Como faria a questão da escolha do usuario para o superuser? Seria qual tipo, fazer um tipo extra que seria todos outros ao mesmo tempo?
class CustomUser(AbstractBaseUser):
    '''
    Modelo para criar um usuario customizado pelo django
    '''
    email = models.EmailField(max_length=100, unique=True)
    user_type = models.CharField(max_length=4,choices=user_type())
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
