from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView, DetailView


# Create your views here.

class HomePage(ListView):
    template_name = 'home.html'
