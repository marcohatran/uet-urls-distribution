import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.config_mail import EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_FROM, EMAIL_TO, \
    SEND_GIRD_KEY
from config.config_mail import list_mails_need_send

import sendgrid
import os
from sendgrid.helpers.mail import *


def send_mail_from_smtp(to, subject, message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP(EMAIL_HOST, 587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

    mailserver.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

    mailserver.quit()


def send_mail_from_sendgird(from_mail, to, subject, message):
    sg = sendgrid.SendGridAPIClient(apikey=SEND_GIRD_KEY)
    from_email = Email(from_mail)
    to_email = Email(to)
    content = Content("text/plain", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    # print(response.body)
    # print(response.headers)
    print('sent mail!')


def send_mail_from_sendgird_to_subscribe_list(from_mail=EMAIL_FROM, list_receivers=list_mails_need_send, subject='', message=''):
    sg = sendgrid.SendGridAPIClient(apikey=SEND_GIRD_KEY)
    from_email = Email(from_mail)
    for to in list_receivers:
        try:
            to_email = Email(to)
            content = Content("text/plain", message)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            # print(response.body)
            # print(response.headers)
            print('sent mail!')
        except Exception as e:
            print(e)


def main():
    # send_mail_from_smtp(to=EMAIL_TO, subject='[BeeCost] Crawled data', message='Crawl xong')
    send_mail_from_sendgird(from_mail=EMAIL_FROM, to=EMAIL_TO, subject='[BeeCost] Crawled data', message='Crawl xong')

# main()
