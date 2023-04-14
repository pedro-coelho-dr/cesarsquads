from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProfileForm, TribeForm, SquadForm
from .models import Tribe, Squad, Profile

#---------
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserAuthenticationForm


# Create your views here.

#TRIBE
def create_tribe(request):
    if request.method == 'POST':
        form = TribeForm(request.POST)
        if form.is_valid():
            tribe = form.save()
            return redirect('detalhes_tribo', tribe_slug=tribe.slug)
    else:
        form = TribeForm()
    return render(request, 'tribe.html', {'form': form})
        
#         return render(request, "tribe.html")


def detalhes_tribo(request, tribe_slug):
    tribe = get_object_or_404(Tribe, slug=tribe_slug)
    return render(request, 'tribe.html', {'tribe': tribe})
# def get_Tribe(request):
#     if request.method == 'GET':
#         return Tribe.name

#def edit_tribe(request):

#def tribe_detail(request):
#    obj = Tribe.objects.get(id=2)
    #context = {
    #    'name': obj.name,
    #}
#    context = {
#        'object': obj,
#    }
#    return render(request,'tribe.html', context)

#SQUAD
def create_squad(request, tribe_slug, squad_slug):
    tribe = get_object_or_404(Tribe, slug=tribe_slug)
    if request.method == 'POST':
        form = SquadForm(request.POST)
        if form.is_valid():
            squad = form.save(commit=False)
            squad.slug = squad_slug
            squad.save()
            return redirect('detalhes_squad', tribe_slug=tribe.slug, squad_slug=squad.slug)
    else:
        form = SquadForm()
    return render(request, 'squad.html', {'form': form, 'tribe': tribe})


def detalhe_squad(request, tribe_slug, squad_slug):
    tribe = get_object_or_404(Tribe, slug=tribe_slug)
    squad = get_object_or_404(Squad, slug=squad_slug, tribe=tribe)
    return render(request, 'squad.html', {'tribe': tribe, 'squad': squad})

#----

def index(request):
    return render(request,'index.html')

@login_required(login_url='login/')
def profile(request):
    list_tribe= Tribe.all()
    return render(request,'profile.html', {"list_tribe": list_tribe})


#--------------------#

#REGISTRO DE USUÁRIO
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            #messages.success(request, f'Conta criada com sucesso para {username}!')
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