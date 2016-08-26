from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


class Register(generic.TemplateView):
    template_name = 'register.html'


class Login(generic.TemplateView):
    template_name = 'login.html'


def loginUser(self, request):
    '''
    Login module for users
    '''
    userName = input("Enter your username")
    passWord = input("Enter your password")

    auth = self.authenticateUser(userName, passWord)  # returns a user object if user is authenticated

    if auth:
        login(request, user)
        # Redirect to a success page
    else:
        pass
        # Return an invalid login error message


def registerUser(request):
# class registerUser(generic.TemplateView):


    '''
    Registration module for new users
    '''
    userName = request.POST['userName']
    passWord = request.POST['passWord']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']

    user = User.objects.create_user(username=userName, password=passWord, first_name=firstName,
            lastname=lastName, email=email)

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


def authenticateUser(self, userName, passWord):
    '''
    Authentication module for users. Takes a user name and password (strings) for arguments.
    Returns a user object if authentication is successful
    '''
    user = authenticate(username=userName, password=passWord)

    if user is not None:
        return user
    else:
        return False


def logoutUser(request):
    '''
    Logout module for users
    '''
    logout(request)
    # Redirect to success page
