from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'pages/home_page.html', {})


def contact(request):
    return render(request, 'pages/contact.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


def faqs(request):
    return render(request, 'pages/faqs.html', {})


def training(request):
    return render(request, 'pages/training.html', {})


def coming_soon(request):
    return render(request, 'pages/coming_soon.html', {})
