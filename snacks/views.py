from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView): 
    ''' responsiple show user the templete'''
    template_name='home.html'