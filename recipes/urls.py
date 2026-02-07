from django.urls import path
from recipes.views import Home, Contact, About

urlpatterns = [
    path('', Home)
]