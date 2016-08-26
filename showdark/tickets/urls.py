from django.conf.urls import url
from . import views

app_name = "tickets"
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^profile', views.Profile.as_view(), name='profile'),
	url(r'^(?P<user_id>[0-9]+)/$', views.get_users_events, name='user_events'),
	url(r'^venues', views.get_all_venues, name='venues'),
]
