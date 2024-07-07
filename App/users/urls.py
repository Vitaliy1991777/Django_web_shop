from django.urls import path

from users import views

from .views import suggestion_view, thank_you_view

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-cart/', views.users_cart, name='users_cart'),
    path('logout/', views.logout, name='logout'),
    path('favorites/', views.favorites, name='favorites'),
    path('suggestions/', suggestion_view, name='suggestions'),
    path('thank_you/', thank_you_view, name='thank_you'),
]

