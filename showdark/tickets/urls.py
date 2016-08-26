from django.conf.urls import url
from . import views

app_name = "tickets"
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<user_id>[0-9]+)/$', views.get_users_events, name='profile'),
	url(r'^venues', views.get_all_venues, name='venues'),
]
