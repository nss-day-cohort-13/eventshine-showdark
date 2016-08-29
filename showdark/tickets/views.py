from django.contrib.auth.models import User, Permission
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from utilities import UtilityConfig


class Register(generic.TemplateView):
    '''
    Handles showing the login page
    '''
    template_name = 'tickets/register.html'


class Login(generic.TemplateView):
    '''
    Handles showing the login page
    '''
    template_name = 'tickets/login.html'


class FailedLogin(generic.TemplateView):
    '''
    Handles showing error page for failed logins
    '''
    template_name = 'tickets/failedLogin.html'


def loginUser(request):
    '''
    Login module for users
    '''
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
    return HttpResponseRedirect('/tickets/login')



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

def create_event(request):
    """
    Creates a new event based on form input from partials/create_event.html UNTESTED

    Args- request object
    """

    # info from create_event.html form; comes in on response object argument
    eventName = request.POST["eventName"]
    description = request.POST["description"]
    city = request.POST["city"]
    startDate = request.POST["startDate"]
    endDate = request.POST["endDate"]
    venue = request.POST["venue"]

    # convert HTML5 datetime-local to python datetime.datetime per Event begin/endTime model requirements
    beginTime = convert_html_datetime_to_python_datetime(startDate)
    endTime = convert_html_datetime_to_python_datetime(endDate)

    event_venue = get_object_or_404(Venue, pk=venue.pk)

    new_event = Event.objects.create(
        name=eventName,
        description=description,
        city=city,
        beginTime=datetime.datetime(beginTime),
        endTime=datetime.datetime(endTime)
    )

    new_event.venue_set.create(pk=event_venue.id)

    return HttpResponse("Create successful!")
