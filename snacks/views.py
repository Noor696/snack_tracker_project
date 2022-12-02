from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Snack

# Create your views here.
class HomePage(TemplateView): 
    ''' responsiple show user the templete'''
    template_name='home.html'

class SnackListView(ListView): 
    template_name='snack_list.html'
    # give it the model we want to show
    model = Snack # the table we want take the data from. 

class SnackDetailView(ListView): 
    template_name='snack_detail.html'
    # give it the model we want to show
    model = Snack # the table we want take the data from. 