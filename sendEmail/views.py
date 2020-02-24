from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

import smtplib


def sendEmail(req):
    checked_res_list = req.POST.getlist('checks')
    inputReceiver = req.POST['inputReceiver']
    inputTitle = req.POST['inputTitle']
    inputContent = req.POST['inputContent']
    restaurants = []

    for checked_res_id in checked_res_list:
        restaurants.append(Restaurant.objects.get(id=checked_res_id))

    content = {'inputContent': inputContent, 'restaurants': restaurants}
    msg_html = render_to_string('sendEmail/email_format.html', content)
    msg = EmailMessage(subject=inputTitle, body=msg_html, from_email="kaeshi9@gmail.com",
                       bcc=inputReceiver.split(','))
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponseRedirect(reverse('index'))