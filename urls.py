# urls.py

from django.urls import path
from .views import BulkEmailView, ScheduleBulkEmailView

urlpatterns = [
     path('send-bulk-emails/', BulkEmailView.as_view(), name='send_bulk_emails'),
     path('schedule-bulk-email/', ScheduleBulkEmailView.as_view(), name='schedule_bulk_email')
]