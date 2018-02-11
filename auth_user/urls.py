from django.conf.urls import  url, include
from . import views
from django.contrib.auth import views as auth_views

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
]