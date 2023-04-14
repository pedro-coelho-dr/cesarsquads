from django import forms
from .models import Profile, Tribe, Squad
from django.forms import ModelForm
#-----
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.text import slugify


#TRIBO
class TribeForm(forms.ModelForm):
    class Meta:
        model = Tribe
        fields = ('name',)
    
    def clean_nome(self):
        name = self.cleaned_data['name']
        slug = slugify(name)
        if Tribe.objects.filter(slug=slug).exists():
            raise forms.ValidationError('Este nome já está em uso.')
        return name

    def save(self, commit=True):
        tribo = super(TribeForm, self).save(commit=False)
        tribo.slug = slugify(tribo.name)
        if commit:
            tribo.save()
        return tribo

#SQUAD
class SquadForm(forms.ModelForm):
    class Meta:
        model = Squad
        fields = ('name',)
        
    def clean_nome(self):
        name = self.cleaned_data['name']
        slug = slugify(name)
        if Squad.objects.filter(slug=slug).exists():
            raise forms.ValidationError('Este nome já está em uso.')
        return name
    
    def save(self, commit=True):
        squad = super(SquadForm, self).save(commit=False)
        squad.slug = slugify(squad.name)
        if commit:
            squad.save()
        return squad


#PERFIL
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar',)

#-------------REGISTRO DE USUÁRIO------------#
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Nome Completo', 'class':"form-control me-2"}))
    username = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Nome de usuário', 'class':"form-control me-2"}))
    email = forms.EmailField(label=False,widget=forms.TextInput(attrs={'placeholder':'Digite seu e-mail', 'class':"form-control me-2"}))
    password1 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Senha', 'class':"form-control me-2"}))
    password2 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Confirmar senha', 'class':"form-control me-2"}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2' )

#AUTENTICAÇÃO DE USUÁRIO--------
class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Usuário', 'class':"form-control me-2"}))
    password = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Senha', 'class':"form-control me-2"}))
    class Meta:
        model = User
        fields = ('username', 'password')

