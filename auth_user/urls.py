from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^login_page', views.login_page, name='login_page'),
    url(r'^logout', views.logout_user, name='logout_user'),
    url(r'^login', views.login_user, name='login_user'),
    url(r'^registration/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^account_activation_success/$', views.account_activation_success, name='account_activation_success'),
]

urlpatterns += [
    url(r'^tinymce/', include('tinymce.urls')),
    ]


# Account management
urlpatterns = [
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
    # profile
    # downloads
]