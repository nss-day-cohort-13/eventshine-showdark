from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core import serializers
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the future login page.")

class Profile(generic.TemplateView):
    template_name = 'tickets/profile.html'

def get_users_events(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	user_events = get_object_or_404(UserEvent, userId=user.id)
	print(user_events)
	data = []
	try:
		for e in user_events:
			event = Event.objects.get(pk=e.eventId)
			data.append(event)
	except TypeError:
		event = Event.objects.get(pk=user_events.eventId.id)
		data.append(event)

	outgoing_data = serializers.serialize("json", data)

	return HttpResponse(outgoing_data, content_type="application/json")

def get_all_venues(request):
	try:
		venues = Venue.objects.all()
		data = serializers.serialize("json", venues)
		return HttpResponse(data, content_type="application/json")
	except:
		return "No venues registered"


