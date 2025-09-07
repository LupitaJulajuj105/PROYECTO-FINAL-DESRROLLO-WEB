from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Homeview(TamplateView):
    template_name = 'home.html'