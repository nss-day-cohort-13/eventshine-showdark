from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the future login page.")

class Profile(generic.TemplateView):
    template_name = 'tickets/profile.html'
