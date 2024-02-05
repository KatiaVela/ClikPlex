from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profile_view

urlpatterns = [
    path('', views.home, name='home'),
    path('About/', views.about, name='about'),
    path('LogIn/', views.login, name='login'),
    path('LogOut/', views.logout, name='logout'),
    path('Contact/', views.contact, name='contact'),
    path('Register/', views.register, name='register'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<int:actor_id>/', views.actor_detail, name='actor_detail'),
    path('reserve/<int:showing_id>/', views.reserve_ticket, name='reserve_ticket'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('accounts/profile/', profile_view, name='profile'),
    path('user-login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='user-login'),

]

