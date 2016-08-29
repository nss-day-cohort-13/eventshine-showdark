from django.conf.urls import url
from . import views


app_name = 'tickets'
urlpatterns = [
	# actual login page
    url(r'^login/', views.Login.as_view(), name='login'),
    url(r'^logout/', views.logoutUser, name='logout'),
	# request.POST data to send user info to login
    url(r'^loginUser/', views.loginUser, name='loginUser'),
	# register page
    url(r'^register/', views.Register.as_view(), name='register'),
	# request.POST to send user data to register
    url(r'^registerUser/', views.registerUser, name='registerUser'),
    url(r'^failedLogin/', views.FailedLogin.as_view(), name='failedLogin'),

	# currently just a string being returned for index
	url(r'^$', views.index, name='index'),

    # url(r'^event/?P<tickets_event.id>[0-9]+)/$')
	# url that appears if login is succesful
    url(r'^profile', views.Profile.as_view(), name='profile'),
	# get request url for user events
    url(r'^(?P<user_id>[0-9]+)/$', views.get_users_events, name='user_events'),
	# get request for all venues
    url(r'^venues', views.get_all_venues, name='venues'),
    url(r'^create_event', views.create_event, name='create_event'),
	# post request to register for an event
	url(r'^event_registration', views.register_for_event, name='event_registration'),
]
