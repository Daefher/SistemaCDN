from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class AgregarForm(UserCreationForm):
    class Meta:
        model = User
        fields = (  'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2',
                 )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Opcional')
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(AgregarForm,self).__init__( *args, **kwargs)
        self.fields['username'].label = "Nombre de Usuario*"
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = "Requerido. 150 caracteres o menos, puede contener, letras, digitos o  @/./+/-/ "
        self.fields['first_name'].label = "Nombre*"
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].label = "Apellido*"
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = "Contraseña*"
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = "Tu contraseña debe contener al menos 8 caracteres y deben ser alfanumericos"
        self.fields['password2'].label = "Confirmar Contraseña*"
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = "Ingrese la misma contraseña"
