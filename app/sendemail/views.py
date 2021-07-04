from django.shortcuts import render
from hello_django.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.

def sendemail(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Covid-19 Information'
        message = 'Register to Covid-19 Contact Tracing'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'registration/success.html', {'recepient': recepient})
    return render(request, 'registration/index.html', {'form':sub})