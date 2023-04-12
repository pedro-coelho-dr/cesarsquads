from django import forms
from .models import Profile
from .models import Tribe
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#REGISTRO DE USUÁRIO
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Nome Completo'}))
    username = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Nome de usuário'}))
    email = forms.EmailField(label=False,widget=forms.TextInput(attrs={'placeholder':'Digite seu e-mail'}))
    password1 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Senha'}))
    password2 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Confirmar senha'}))
    
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2' )

#AUTENTICAÇÃO DE USUÁRIO
class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Usuário'}))
    password = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Senha'}))
    class Meta:
        model = User
        fields = ('username', 'password')

#PERFIL
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar')

#SQUAD

#TRIBO
class TribeForms(forms.ModelForm):
    class Meta:
        model = Tribe
        fields = ['name',]