from rest_framework import serializers
from .models import *
from django.conf import settings
from rest_framework.validators import UniqueTogetherValidator

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class shopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = shop
        fields =  '__all__'
class reviewSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):   
        rev_instance = review.objects.create(**validated_data)
        # Example usage
        subject = 'NK Review System'
        body = 'Your review has been created.'
        to_email = validated_data.get('email')

        self.send_email(subject, body, to_email)
        return rev_instance
    def send_email(self,subject, body, to_email): 
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465
        smtp_username = 'your@gmail.com'  # Your Gmail email address
        smtp_password = 'your gmail app password'  # Your Gmail password or app-specific password

        # Email content
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Establish a connection to the SMTP server
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            # Start TLS for security 

            # Log in to the email account
            server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(smtp_username, to_email, msg.as_string())
    class Meta:
        model = review
        fields =  '__all__'