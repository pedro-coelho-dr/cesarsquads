from django.urls import path
from cesarsquads import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.Login, name='index'),
    path('login/', views.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name ='register'),
    path('profile/', views.profile, name ='profile'),
    path('tribe/<slug:tribe_slug>/', views.detalhes_tribo, name='detalhes_tribo'),
    path('tribe/<slug:tribe_slug>/entrar/', views.entrar_tribo, name='entrar_tribo'),
    path('tribe/', views.create_tribe, name ='create_tribe'),
    path('tribe/<slug:tribe_id>/squad/', views.create_squad, name='squad'),
    path('tribe/<slug:tribe_id>/squad/<slug:squad_slug>/', views.detalhes_squad, name='detalhes_squad'),
    path('tribe/<slug:tribe_id>/squad/<slug:squad_slug>/entrar/', views.entrar_squad, name='entrar_squad'),
    path('search/', views.search_tribe, name='search_tribe'),

]