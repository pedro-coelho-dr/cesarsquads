from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Squad, Tribe
from crispy_forms.helper import FormHelper
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = False
        self.fields['password2'].label = False
        self.fields['username'].label = False
        self.fields['password1'].placeholder = 'Senha'
        self.fields['password2'].placeholder = 'Confirme sua senha'
        self.fields['username'].placeholder = 'Usuário'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2' )


#        help_texts = {
 #           'username': None,
  #      }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
        
#class SquadForm(forms.ModelForm):
    