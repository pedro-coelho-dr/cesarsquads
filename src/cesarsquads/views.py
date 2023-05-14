from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProfileForm, TribeForm, SquadForm
from .models import Tribe, Squad, Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserAuthenticationForm
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse
from PIL import Image
import os


# Create your views here.

#TRIBE
def create_tribe(request):
    if request.method == 'POST':
        form = TribeForm(request.POST)
        nome_tribo = form.data['name'] 
        if Tribe.objects.filter(name=nome_tribo).exists():
            messages.error(request, 'Esta tribo ja existe! Tente outro nome, ou procure a tribo na barra de pesquisa.')
            profile_url = reverse('profile')  
            return redirect(profile_url)
        else: 
            if form.is_valid():
                tribe = form.save()
                tribe.members.add(request.user)
                return redirect('detalhes_tribo', tribe_slug=tribe.slug)
    else:
        form = TribeForm()
    return render(request, 'tribe.html', {'form': form})
        

def detalhes_tribo(request, tribe_slug):
    tribe = get_object_or_404(Tribe, slug=tribe_slug)
    try:
        tribe = Tribe.objects.get(slug=tribe_slug)
    except Tribe.DoesNotExist:
        return HttpResponse("Tribo não encontrada!")
    if request.method == 'POST':
        bio = request.POST.get('bio')
        tribe.bio = bio
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            
            image = Image.open(avatar)
            image = image.convert('RGB')
            max_size = (500, 500)
            image.thumbnail(max_size)
            
            original_path, original_filename = os.path.split(avatar.name)
            resized_avatar_filename = f"{tribe_slug}_resized.jpg"
            resized_avatar_path = os.path.join('tribe', resized_avatar_filename)
            resized_avatar_full_path = os.path.join(settings.MEDIA_ROOT, resized_avatar_path)
            image.save(resized_avatar_full_path, optimize=True, quality=95)
            
            tribe.avatar.name = resized_avatar_path

        tribe.save()
        return redirect('detalhes_tribo', tribe_slug=tribe.slug)
    squads = Squad.objects.filter(tribe=tribe)
    
    return render(request, 'tribe.html', {'tribe': tribe, 'list_squad': squads})


def entrar_tribo(request, tribe_slug):
    if request.method == 'POST':
        if request.POST.get('action') == 'entrar':
            tribe_name = request.POST.get('tribe_name')
            try:
                tribe = Tribe.objects.get(name=tribe_name)
                return redirect('detalhes_tribo', tribe_slug=tribe.slug)
            except Tribe.DoesNotExist:
                return redirect('pagina_erro')
    else:
        tribe = get_object_or_404(Tribe, slug=tribe_slug)
        tribe.members.add(request.user)
    return redirect('detalhes_tribo', tribe_slug=tribe.slug)


def search_tribe(request):
    query = request.GET.get('tribe_search')
    tribes = Tribe.objects.filter(name__icontains=query)
    return render(request, 'search_tribe.html', {'tribes': tribes})





#SQUAD
def create_squad(request, tribe_id):
    tribe = get_object_or_404(Tribe, id=tribe_id)
    if request.method == 'POST':
        form = SquadForm(request.POST)
        nome_squad = form.data['name']
        if Squad.objects.filter(name=nome_squad, tribe_id=tribe_id).exists():
            messages.error(request, 'Já existe uma squad com este nome nesta tribo.')
            return redirect('detalhes_tribo', tribe_slug=tribe.slug)
        
        else:
            if form.is_valid():  
                squad = form.save(commit=False)
                squad.tribe_id = tribe_id
                squad.save()
                squad.members.add(request.user)
                return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=tribe.id)
    else:
        form = SquadForm()
    return render(request, 'squad.html', {'form': form})


def detalhes_squad(request, squad_slug, tribe_id):
    squad = get_object_or_404(Squad, slug=squad_slug, tribe_id=tribe_id)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        squad.bio = bio
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            
            image = Image.open(avatar)
            image = image.convert('RGB')
            max_size = (500, 500)
            image.thumbnail(max_size)
            
            original_path, original_filename = os.path.split(avatar.name)
            resized_avatar_filename = f"{squad_slug}_resized.jpg"
            resized_avatar_path = os.path.join('squad', resized_avatar_filename)
            resized_avatar_full_path = os.path.join(settings.MEDIA_ROOT, resized_avatar_path)
            image.save(resized_avatar_full_path, optimize=True, quality=95)
            
            squad.avatar.name = resized_avatar_path

        squad.save()
        return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=tribe_id)
    return render(request, 'squad.html', {'squad': squad, 'tribe_id': tribe_id})

def entrar_squad(request, squad_slug, tribe_id):
    squad = get_object_or_404(Squad, slug=squad_slug, tribe_id=tribe_id)
    squad.members.add(request.user)
    return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=squad.tribe.id)

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