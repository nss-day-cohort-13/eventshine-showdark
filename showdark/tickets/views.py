from django.contrib.auth.models import User, Permission
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from .utilities import *
import json
import ast


class Login(generic.TemplateView):
    '''
    Handles showing the login page
    '''
    template_name = 'tickets/index.html'


class Register(generic.TemplateView):
    '''
    Handles showing the login page
    '''
    template_name = 'tickets/register.html'


class FailedLogin(generic.TemplateView):
    '''
    Handles showing error page for failed logins
    '''
    template_name = 'tickets/failedLogin.html'


def loginUser(request):
    '''
    Login module for users
    '''
    print("~~USER~~")
    userName = request.POST['userName']
    passWord = request.POST['passWord']
    auth = authenticate(username=userName, password=passWord)

    if auth:
        try:
            user = authenticateUser(request, userName, passWord)  # returns a user object if user is authenticated
            login(request, user)
            return render(request, 'tickets/profile.html')
        except:  # I dont know what the exception would be if the user authentication works but the login doesn't
            return HttpResponseRedirect('../failedLogin/')
    else:
        return HttpResponseRedirect('../failedLogin/')

def get_current_user(request):
    user = serializers.serialize("json", [request.user,])
    return HttpResponse(user, content_type="application/json")


def authenticateUser(request, userName, passWord):
    '''
    Authentication module for users. Takes a user name and password (strings) for arguments.
    Returns a user object if authentication is successful
    '''
    user = authenticate(username=userName, password=passWord)

    if user is not None:
        return user
    else:
        return False


def registerUser(request):
    '''
    Registration module for new users
    '''
    userName = request.POST['userName']
    passWord = request.POST['passWord']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']

    user = User.objects.create_user(username=userName, password=passWord, first_name=firstName,
                                    last_name=lastName, email=email)

    # Permissions
    # Add
    user.has_perm('tickets.add_Venue')
    user.has_perm('tickets.add_Event')
    user.has_perm('tickets.add_UserEvent')
    # Change
    user.has_perm('tickets.change_Venue')
    user.has_perm('tickets.change_Event')
    user.has_perm('tickets.change_UserEvent')
    # Delete
    user.has_perm('tickets.delete_Venue')
    user.has_perm('tickets.delete_Event')
    user.has_perm('tickets.delete_UserEvent')

    user.save()
    return HttpResponseRedirect('/tickets/profile')


def logoutUser(request):
    '''
    Logout module for users
    '''
    logout(request)
    # Redirect to success page
    return HttpResponseRedirect('/tickets/')


def index(request):
    return HttpResponse("Hello, world. You're at the future login page.")


class Profile(generic.TemplateView):
    template_name = 'tickets/profile.html'


def get_users_events(request, user_id):
    """
    Gets all events logged-in user has registered for

    Args- request object, logged-in user's id
    """

    user = get_object_or_404(User, pk=user_id)
    user_events = get_list_or_404(UserEvent, userId=user.id)
    data = []
    try:
        for e in user_events:
            event = Event.objects.get(pk=e.eventId.id)
            data.append(event)
    except TypeError:
        event = Event.objects.get(pk=user_events.eventId.id)
        data.append(event)

    outgoing_data = serializers.serialize("json", data)

    return HttpResponse(outgoing_data, content_type="application/json")


def get_all_venues(request):

    """
    Gets all registered venues

    Args- request object
    """
    try:
        venues = Venue.objects.all()
        data = serializers.serialize("json", venues)
        return HttpResponse(data, content_type="application/json")
    except:
        return HttpResponse("No venues registered")

def get_all_events(request):
    """
    Returns json data of all events
    """
    events = Event.objects.all()
    data = serializers.serialize("json", events)
    return HttpResponse(data, content_type="application/json")


def create_event(request):
    """
    Creates a new event based on form input from partials/create_event.html UNTESTED

    Args- request object
    """

    # info from create_event.html form; comes in on response object argument
    data = request.body.decode("utf-8")
    data2 = json.loads(data)

    eventName = data2["eventName"]
    description = data2["description"]
    city = data2["city"]
    beginTime = data2["beginTime"]
    endTime = data2["endTime"]
    venueId = data2["venue"]

    event_venue = get_object_or_404(Venue, pk=venueId)

    new_event = Event.objects.create(
        name=eventName,
        description=description,
        city=city,
        beginTime=beginTime,
        endTime=endTime,
        venueId=event_venue
    )

    new_event.save()

    return HttpResponse("Event created")


def register_for_event(request):
    """
    Registers logged-in user for selected event

    Args- request object (via POST, comes in as JSON)
    """

    data = request.body.decode('utf-8')
    data2 = json.loads(data)
    user_id = data2['user_id']
    event_id = data2['event_id']
    user = User.objects.get(pk=user_id)
    event = Event.objects.get(pk=event_id)
    venue = Venue.objects.get(pk=event.venueId.id)
    registered_event = UserEvent.objects.create(userId=user, eventId=event)
    event.tickets_sold += 1
    event.save()
    if event.tickets_sold == venue.capacity:
        event.full = 1
        event.save()
    return HttpResponse("Registration Successful")
