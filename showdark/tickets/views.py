from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'tickets/index.html'
