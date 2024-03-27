# tasks.py (inside one of your Django apps)

import os
from celery import Celery  # Import Celery app instance
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime  # Add this import

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')

# Using a string here means the worker doesn't have to serialize the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@shared_task
def send_bulk_emails(subject, message):
    users = User.objects.filter(email__isnull=False).exclude(email__exact='')  
    # Filter users with valid emails
    emails = [user.email for user in users if user.email]
    
    batch_size = 100  # Adjust the batch size as per your requirements
    for i in range(0, len(emails), batch_size):
        batch_emails = emails[i:i+batch_size]
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, batch_emails)
        except Exception as e:
            # Log the error properly
            print(f"Error sending emails: {str(e)}")

@shared_task
def schedule_bulk_email(subject, message, scheduled_time):
    now = datetime.now()
    if scheduled_time > now:
        send_bulk_emails.apply_async((subject, message), eta=scheduled_time)
    else:
        print("Scheduled time should be in the future.")
