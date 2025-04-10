from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('browse/', browse, name="browse"),
    path('details/', details, name="details"),
    path('streams/', streams, name="streams"),
    path('profile/', profile, name="profile")
]