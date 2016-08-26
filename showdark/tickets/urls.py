from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    # url(r'^login/', views.Login.as_view(), name="login"),
    # url(r'^loginUser/', views.loginUser, name="loginUser"),
    url(r'^register/', views.Register.as_view(), name="register"),
    url(r'^registerUser/', views.registerUser, name="registerUser"),
    #
    # lines for urls with json data
    #
]
