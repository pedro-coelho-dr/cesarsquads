from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Squad, Tribe

#REGISTRO DE USUÁRIO
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Nome de usuário'}))
    password1 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Senha'}))
    password2 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Confirmar senha'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2' )

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
        fields = ['bio', 'avatar']

#SQUAD

#TRIBO
