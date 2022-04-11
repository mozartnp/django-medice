from django import forms
from django.contrib.auth.forms import UserCreationForm

from backend.custom_user.models import CustomUser


class SignupForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'user_type',
            'password1',
            'password2'
        )
        labels = {
            'user_type': 'Tipo de cadastro'
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Digite seu e-mail.',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Sua senha deve conter A-Z a-z 0-9',
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Repita sua senha.',
            }
        )


class AutencicandoUser(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': "Digite seu e-mail"}
        )
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={'placeholder': "Digite sua senha"}
        )
    )
