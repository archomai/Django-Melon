from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render


def send_email(request):
    if request.method == 'POST':
        email = EmailMessage(
            request.POST.get('subject'),
            request.POST.get('message'),
            to=[request.POST.get('email')],
        )
        email.send()
    return render(request, 'emails/send_email.html')
