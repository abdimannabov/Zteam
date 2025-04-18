from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('browse/', browse, name="browse"),
    path('details/<int:pk>/', details, name="details"),
    path('streams/', streams, name="streams"),
    path('profile/', profile, name="profile"),
    path('login/', user_login, name="login"),
    path('signin/', signin, name="signin"),
    path('register/', user_register, name="register"),
    path('singup', signup, name="signup"),
    path('logout/', user_logout, name="logout"),
]