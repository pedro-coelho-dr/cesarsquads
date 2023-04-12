from django.urls import path
from cesarsquads import views 
from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name ='register'),
    path('profile/', views.profile, name ='profile'),
    path('tribe/', views.create_tribe, name ='tribe'),
    path('squad/', views.create_squad, name ='squad'),
]