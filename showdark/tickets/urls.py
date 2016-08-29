from django.conf.urls import url
from . import views


app_name = 'tickets'
urlpatterns = [
    url(r'^login/', views.Login.as_view(), name="login"),
    url(r'^loginUser/', views.loginUser, name="loginUser"),
    url(r'^register/', views.Register.as_view(), name="register"),
    url(r'^registerUser/', views.registerUser, name="registerUser"),
    url(r'^failedLogin/', views.FailedLogin.as_view(), name='failedLogin'),
    url(r'^$', views.index, name='index'),
    #
    # lines for urls with json data
    #
    url(r'^$', views.index, name='index'),
    url(r'^profile', views.Profile.as_view(), name='profile'),
    url(r'^(?P<user_id>[0-9]+)/$', views.get_users_events, name='user_events'),
    url(r'^venues', views.get_all_venues, name='venues'),
	url(r'^(?P<user_id>\d+)/(?P<event_id>\d+)$', views.register_for_event, name='event_registration'),
]
