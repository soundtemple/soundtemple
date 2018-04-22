from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

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
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']

            template = get_template('pages/contact_template.txt')

            context = {
                'name': name,
                'from_email': from_email,
                'mobile': mobile,
                'subject': subject,
                'message': message,
            }

            content = template.render(context)

            try:
                email = EmailMessage(
                                     body=content,
                                     subject='New Sountemple Contact form submission',
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
