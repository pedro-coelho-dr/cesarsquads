from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm, TribeForm, SquadForm
from .models import Tribe, Squad, Profile

#---------
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserAuthenticationForm


# Create your views here.

#TRIBO
def create_tribe(request):
    if request.method == 'POST':
        form = TribeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'tribe.html', {'form': form })
#         return render(request, "tribe.html")

#def edit_tribe(request):

def tribe_detail(request):
    obj = Tribe.objects.get(id=2)
    #context = {
    #    'name': obj.name,
    #}
    context = {
        'object': obj,
    }
    return render(request,'tribe.html', context)

#SQUAD
def create_squad(request):
    if request.method == 'POST':
        form = SquadForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'squad.html', {'form': form })
#         return render(request, "tribe.html")

#def edit_tribe(request):

def squad_detail(request):
    return render(request,'squad.html')

#----

def index(request):
    return render(request,'index.html')

@login_required(login_url='login/')
def profile(request):
    return render(request,'profile.html')


#--------------------#

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