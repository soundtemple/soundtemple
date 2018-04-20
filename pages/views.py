from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


# Create your views here.


def home_page(request):
    return render(request, 'pages/home_page.html', {})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            reference = 'STW-MSG: '
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            if form.cleaned_data['mobile']:
                mobile = form.cleaned_data['email']
            else:
                mobile = 'No mobile supplied'
            message = form.cleaned_data['message']
            try:
                email = EmailMessage(
                                     body=reference + message,
                                     subject=subject,
                                     from_email=from_email,
                                     to=['info@soundtemple.com.au'],
                                     headers={'Reply-To': from_email},
                                     cc=[from_email],
                                     )
                email.send()
            except BadHeaderError:
                return HttpResponse('There was a problem with your details')
            request.session['temp_data'] = form.cleaned_data
            return redirect('contact_success')
    return render(request, 'pages/contact.html', {'form': form})


def contact_success(request):
    form_details = request.session['temp_data']
    return render(request, 'pages/contact_success.html', {'form_details':form_details})


def about(request):
    return render(request, 'pages/about.html', {})


def faqs(request):
    return render(request, 'pages/faqs.html', {})


def training(request):
    return render(request, 'pages/training.html', {})


def coming_soon(request):
    return render(request, 'pages/coming_soon.html', {})
