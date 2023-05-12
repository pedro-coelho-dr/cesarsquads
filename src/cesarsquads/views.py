from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProfileForm, TribeForm, SquadForm
from .models import Tribe, Squad, Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserAuthenticationForm
from django.http import HttpResponse


# Create your views here.

#TRIBE
def create_tribe(request):
    if request.method == 'POST':
        form = TribeForm(request.POST)
        if form.is_valid():
            tribe = form.save()
            tribe.members.add(request.user)
            return redirect('detalhes_tribo', tribe_slug=tribe.slug)
    else:
        form = TribeForm()
    return render(request, 'tribe.html', {'form': form})
        

def detalhes_tribo(request, tribe_slug):
    tribe = get_object_or_404(Tribe, slug=tribe_slug)
    squads = Squad.objects.filter(tribe=tribe)
    return render(request, 'tribe.html', {'tribe': tribe, 'list_squad': squads})


#SQUAD
def create_squad(request, tribe_id):
    if request.method == 'POST':
        form = SquadForm(request.POST)
        if form.is_valid():
            squad = form.save(commit=False)
            squad.tribe_id = tribe_id  # Associa o ID da tribo à squad
            squad.save()
            squad.members.add(request.user)
            return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=tribe_id)
    else:
        form = SquadForm()
    return render(request, 'squad.html', {'form': form})


def detalhes_squad(request, squad_slug, tribe_id):
    squad = get_object_or_404(Squad, slug=squad_slug, tribe__id=tribe_id)
    return render(request, 'squad.html', {'squad': squad})

def entrar_squad(request, squad_slug, tribe_id):
    squad = get_object_or_404(Squad, slug=squad_slug, tribe_id=tribe_id)
    squad.members.add(request.user)
    return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=squad.tribe.id)


# def enter_squad(request, squad_slug):
#     squad = get_object_or_404(Squad, slug=squad_slug)
#     if request.method == 'POST':
#         entered_slug = request.POST.get('slug')
#         if entered_slug == squad.slug:
#             # Adicione o usuário ao esquadrão
#             squad.members.add(request.user)
#             messages.success(request, 'Você entrou no squad {{squad.slug}} com sucesso!')
#             return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=squad.tribe_id)
#         else:
#             messages.error(request, 'Squad inexistente ou inválida!')
#     return render(request, 'squad.html', {'squad': squad})

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