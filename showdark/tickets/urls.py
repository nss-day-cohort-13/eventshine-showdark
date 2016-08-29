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
    url(r'^profile', views.Profile.as_view(), name='profile'),

    #
    # lines for urls with json data
    #
]
