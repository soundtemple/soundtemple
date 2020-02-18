from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^contact_success$', views.contact_success, name='contact_success'),
    url(r'^about$', views.about, name='about'),
    url(r'^faqs$', views.faqs, name='faqs'),
    url(r'^training', views.training, name='training'),
    url(r'^coming_soon', views.coming_soon, name='coming_soon'),
    path('upload/', views.DocumentCreateView.as_view(), name='upload_doc'),
]