from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.


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


def index(request):
    return HttpResponse("Hello, world. You're at the future login page.")


class Profile(generic.TemplateView):
    template_name = 'tickets/profile.html'
