from django.urls import path,include
from django.conf import settings
from . import views as user_view
from django.conf.urls.static import static
from django.contrib.auth import views as auth

urlpatterns = [
    path('', user_view.index, name='index'),
    path('login/', user_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', user_view.register, name ='register'),
    path('profile/', user_view.profile, name ='profile'),
]