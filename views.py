# views.py (inside one of your Django apps)

from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_bulk_emails, schedule_bulk_email
from datetime import datetime

class BulkEmailView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        send_bulk_emails.delay(subject, message)
        return Response({"message": "Bulk emails sent successfully!"})
    
class ScheduleBulkEmailView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        scheduled_time_str = request.data.get('scheduled_time')
        
        try:
            scheduled_time = datetime.strptime(scheduled_time_str, '%Y-%m-%d %H:%M:%S')
            schedule_bulk_email.delay(subject, message, scheduled_time)
            return Response({"message": "Bulk email scheduled successfully!"})
        except ValueError:
            return Response({"message": "Invalid scheduled time format. Use YYYY-MM-DD HH:MM:SS."}, status=400)