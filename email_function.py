#!/usr/bin/env python
# coding: utf-8
# Author: @jackexu https://github.com/jackexu

import smtplib
from email.mime.text import MIMEText

def send_email(gmail_user, gmail_password, sender, receivers, subject_text, email_text):
    """
    You need to deactivate your Gmail 2FA setting and allow Less Secure App

    :param gmail_user: String. Your Gmail username - those before @gmail.com
    :param gmail_password: String. Your Gmail password - !!make sure!! you remove it before send this file to others!!!!
    :param sender: String. Sender's full email address: e.g. 'aa@gmail.com'
    :param receivers: List. Email address in string format in list: e.g. ['aa@gmail.com','bb@gmail.com']
    :param subject_text: String
    :param email_text: String
    :return: Email sending status

    """

    # Build Message
    msg = MIMEText(email_text)
    msg['Subject'] = subject_text
    msg['From'] = sender
    msg['To'] = ", ".join(receivers)
    # email send request
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sender, receivers, msg.as_string())
        server.close()
        print('Email sent!')
    except Exception as e:
        print(e)
        print('Something went wrong...')


