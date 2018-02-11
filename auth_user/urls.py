from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^login_page', views.login_page, name='login_page'),
    url(r'^logout', views.logout_user, name='logout_user'),
    url(r'^login', views.login_user, name='login_user')
]