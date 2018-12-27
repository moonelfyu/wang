from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.index, name="logout"),
    url(r'^index/$', views.index, name="index"),
    url(r'^login/$', views.login, name="login"),
    url(r'^login_handle/$', views.login_handle, name="login_handle"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^contact/$', views.contact),
    url(r'^register/submit', views.submit),
    url(r'^submit/?$', views.submit),
    url(r'^usr_info/?$', views.usr_info, name="usr_info"),
    url(r'^content/?$', views.content, name="content"),



]