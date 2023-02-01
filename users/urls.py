from django.urls import path
from .views import LoginView, register, LogOut


urlpatterns = [
    path('',LoginView, name='login'),
    path('signup/',register.as_view(), name='signup'),
    path('logout/',LogOut, name='logout'),
]
