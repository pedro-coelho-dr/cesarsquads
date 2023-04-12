from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserAuthenticationForm
from .forms import TribeForms
from .models import Tribe

# Create your views here.

def index(request):
    return render(request,'index.html')

#REGISTRO DE USUÁRIO
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Conta criada com sucesso para {username}!')            
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form, 'title':'Registro'})

# AUTENTICAÇÃO DE USUÁRIO
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('profile')
        else:
            messages.info(request, f'Usuário ou senha inválido!')
    form = UserAuthenticationForm()
    return render(request, 'registration/login.html', {'form':form, 'title':'Login'})

@login_required(login_url='login/')
def profile(request):
    return render(request,'profile.html')

def tribe(request): 
    if request.method == 'POST':
        form = TribeForms(request.POST)  
        if form.is_valid():
            tribe = Tribe(**form.cleaned_data)
            tribe.save()
            messages.success(request, f'Tribo criada com sucesso!')
    return render(request, 'tribe.html')

   #TRIBE criada com link de acesso
#def create_tribe(request):

    #SQUAD adicionado a TRIBE
#def create_squad(request):

    #SQUAD removido de TRIBE
#def delete_squad(request):

    #USER entra na SQUAD
#def join_squad(request):

    #USER sai de SQUAD
#def exit_squad(request):