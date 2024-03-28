from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from settings.models import UserDetails
import pytz

# @shared_task
# def send_bulk_emails(subject, message):
#     print('hello')
#     users=UserDetails.objects.all()
#     emails=[user.email for user in users]
#     batch_size=100
#     for i in range(0, len(emails), batch_size):
#         batch_emails=emails[i:i+batch_size]
#         try:
#             send_mail(subject, message, settings.EMAIL_HOST_USER, batch_emails)
#         except Exception as e:
#             print(f"error sending emails: {str(e)}")    

# @shared_task
# def schedule_bulk_email(subject,message, schedule_time):
#     now=datetime.now()
#     print(now)
#     if schedule_time>now:
#         send_bulk_emails.delay(subject, message)
#     else:
#         print("Schedule time should be in the future.")

"""1) The above version is more efficient for handling a large number of emails as it distributes 
the workload across multiple tasks. However, it doesn't schedule tasks at the exact schedule_time.

2) The below version ensures correctness by scheduling tasks to run at the exact schedule_time. 
However, it may not be the most efficient approach for handling a large number of emails."""

@shared_task
def send_bulk_emails(subject, message, emails):
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, emails)
    except Exception as e:
        print(f"error sending emails: {str(e)}")    

@shared_task
def schedule_bulk_email(subject, message, schedule_time):
    timezone=pytz.timezone('Asia/Kolkata')
    now = datetime.now(timezone)
    if schedule_time > now:
        delta=(schedule_time-now).total_seconds()
        users = UserDetails.objects.all()
        emails = [user.email for user in users]
        # batch_size = 100
        # for i in range(0, len(emails), batch_size):
        #     batch_emails = emails[i:i + batch_size]
        send_bulk_emails.apply_async((subject, message, emails), countdown=delta)
    else:
        print("Schedule time should be in the future.")


