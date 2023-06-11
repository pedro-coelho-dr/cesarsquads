from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProfileForm, TribeForm, SquadForm
from .models import Tribe, Squad, Profile
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserAuthenticationForm, UserSearchForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
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
    avatar_upload_error = None
    
    try:
        tribe = Tribe.objects.get(slug=tribe_slug)
    except Tribe.DoesNotExist:
        return HttpResponse("Tribo não encontrada!")
    
    if request.method == 'POST':
        bio = request.POST.get('bio')
        tribe.bio = bio
        
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            
            if not avatar.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                avatar_upload_error = 'Tipo de arquivo inválido. Por favor, faça o upload de um arquivo JPG, JPEG ou PNG.'
            
            if avatar.size > 5 * 1024 * 1024:
                avatar_upload_error = 'O tamanho do arquivo excede o limite de 5MB.'
            
            if not avatar_upload_error:
                try:
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
                
                except (OSError, ValidationError):
                    avatar_upload_error = 'Erro ao processar o arquivo de imagem.'
        
        if not avatar_upload_error:
            tribe.save()
            return redirect('detalhes_tribo', tribe_slug=tribe.slug)
    
    squads = Squad.objects.filter(tribe=tribe)
    
    return render(request, 'tribe.html', {'tribe': tribe, 'list_squad': squads, 'avatar_upload_error': avatar_upload_error})


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





@login_required(login_url='login/')
def add_user_to_tribe(request, tribe_slug):
    tribe = get_object_or_404(Tribe, slug=tribe_slug)
    User = get_user_model()

    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            tribe.members.add(user)
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')

    return redirect('detalhes_tribo', tribe_slug=tribe.slug)


@login_required(login_url='login/')
def remove_user_from_tribe(request, tribe_slug):
    tribe = get_object_or_404(Tribe, slug=tribe_slug)
    User = get_user_model()

    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        user_id = form.data['user_id']
        if User.objects.filter(id=user_id).exists():
            user = User.objects.get(id=user_id)

            for squad in tribe.squad_set.all():
                if user in squad.members.all():
                    squad.members.remove(user)

            tribe.members.remove(user)
        else:
            messages.error(request, 'Usuário não encontrado.')

    return redirect('detalhes_tribo', tribe_slug=tribe.slug)




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
    avatar_upload_error = None
    
    if request.method == 'POST':
        bio = request.POST.get('bio')
        squad.bio = bio
        
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            
            if not avatar.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                avatar_upload_error = 'Tipo de arquivo inválido. Por favor, faça o upload de um arquivo JPG, JPEG ou PNG.'
            
            if avatar.size > 5 * 1024 * 1024:
                avatar_upload_error = 'O tamanho do arquivo excede o limite de 5MB.'
            
            if not avatar_upload_error:
                try:
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
                
                except (OSError, ValidationError):
                    avatar_upload_error = 'Erro ao processar o arquivo de imagem.'
        
        if not avatar_upload_error:
            squad.save()
            return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=tribe_id)
    
    return render(request, 'squad.html', {'squad': squad, 'tribe_id': tribe_id, 'avatar_upload_error': avatar_upload_error})

def entrar_squad(request, squad_slug, tribe_id):
    squad = get_object_or_404(Squad, slug=squad_slug, tribe_id=tribe_id)
    squad.members.add(request.user)
    return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=squad.tribe.id)

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
@login_required(login_url='login/')
def add_user_to_squad(request, squad_slug, tribe_id):
    squad = get_object_or_404(Squad, slug=squad_slug, tribe_id=tribe_id)
    User = get_user_model()
    
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        username = form.data['username']
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            squad.members.add(user)
            
            # Verificar se o usuário já é membro da tribo
            if not squad.tribe.members.filter(id=user.id).exists():
                squad.tribe.members.add(user)
        else:
            messages.error(request, 'Usuário não encontrado.')
        
    return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=tribe_id)


@login_required(login_url='login/')
def remove_user_from_squad(request, squad_slug, tribe_id):
    squad = get_object_or_404(Squad, slug=squad_slug, tribe_id=tribe_id)

    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        user_id = form.data['user_id']
        CustomUser = get_user_model()
        if CustomUser.objects.filter(id=user_id).exists():
            user = CustomUser.objects.get(id=user_id)
            squad.members.remove(user)  # Usando remove() para remover o usuário da squad
        else:
            messages.error(request, 'Usuário não encontrado.')

    return redirect('detalhes_squad', squad_slug=squad.slug, tribe_id=tribe_id)

#----
def sair_squad(request, squad_slug, tribe_id):
    squad = get_object_or_404(Squad, slug=squad_slug, tribe_id=tribe_id)
    user = request.user
    squad.members.remove(user)
    tribe_slug = squad.tribe.slug if squad.tribe else None
    return redirect('detalhes_tribo', tribe_slug=tribe_slug)

def index(request):
    return render(request,'index.html')

@login_required(login_url='login/')
def profile(request):
    if request.method == 'POST':
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']

            avatar_upload_error = None
            
            if not avatar.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                avatar_upload_error = 'Tipo de arquivo inválido. Por favor, faça o upload de um arquivo JPG, JPEG ou PNG.'
            
            elif avatar.size > 5 * 1024 * 1024:
                avatar_upload_error = 'O tamanho do arquivo excede o limite de 5MB.'
            
            if not avatar_upload_error:
                try:
                    image = Image.open(avatar)
                    image = image.convert('RGB')
                    max_size = (500, 500)
                    image.thumbnail(max_size)
                    
                    original_path, original_filename = os.path.split(avatar.name)
                    resized_avatar_filename = f"{request.user.username}_resized.jpg"
                    resized_avatar_path = os.path.join('profile_images', resized_avatar_filename)
                    resized_avatar_full_path = os.path.join(settings.MEDIA_ROOT, resized_avatar_path)
                    image.save(resized_avatar_full_path, optimize=True, quality=95)
                    
                    request.user.profile.avatar.name = resized_avatar_path
                    request.user.profile.save()
                except (OSError, ValidationError):
                    avatar_upload_error = 'Erro ao processar o arquivo de imagem.'
            
            if avatar_upload_error:
                messages.error(request, avatar_upload_error)
            else:
                messages.success(request, 'Seu avatar foi atualizado!', extra_tags='avatar_updated')

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

