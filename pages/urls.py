from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^faqs$', views.faqs, name='faqs'),
    url(r'^training', views.training, name='training'),
    url(r'^coming_soon', views.coming_soon, name='coming_soon'),
]