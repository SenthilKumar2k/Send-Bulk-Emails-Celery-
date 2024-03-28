from orders.tasks import send_bulk_emails, schedule_bulk_email
import pytz
from datetime import datetime

class BulkEmailView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request):
        print('hello')
        subject=request.data.get('subject')
        message=request.data.get('message')
        send_bulk_emails.delay(subject, message)
        return Response({"message":"Bulk email send successfully !"})


class ScheduleBulkEmailView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request):
        subject=request.data.get('subject')
        message=request.data.get('message')
        scheduled_time_str=request.data.get('scheduled_time')
        timezone=pytz.timezone("Asia/Kolkata")
        try:
            scheduled_time=datetime.strptime(scheduled_time_str, "%Y-%m-%d %H:%M:%S")
            scheduled_time=timezone.localize(scheduled_time)
            schedule_bulk_email.delay(subject, message, scheduled_time)
            return Response({"message":"Bulk Email sheduled successfully!"})
        except ValueError:
            return Response({"message":"Invalid schedule time format. Use YYYY-MM-DD HH:MM:SS"}, status=400)
