from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile', views.Profile.as_view(), name='profile'),
    #
    # lines for urls with json data
    #
]
