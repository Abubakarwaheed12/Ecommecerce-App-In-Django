# Libs
from django.core.mail import send_mail
import uuid
from django.conf import settings

#  Function For Sending Fogot Password Mails
def send_fogot_password_mail(email , token):
    subject='Your Forgot Password Link'
    message=f'HI click on the link to reset you password http://127.0.0.1:8000/accounts/resetPassword/{token}/'
    from_eamil=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject, message, from_email, recipient_list)
    
    return True