from django.apps import AppConfig

class TicketsConfig(AppConfig):
    name = 'tickets'

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

    def logoutUser(request):
        '''
        Logout module for users
        '''
        logout(request)
        # Redirect to success page


