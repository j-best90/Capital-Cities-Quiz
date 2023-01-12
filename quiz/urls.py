from django.urls import  path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/<str:randomCountry>/<str:capitalAnswer>', views.results, name='results'),
]