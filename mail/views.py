from django.http import HttpResponse
from .utils import send_mail_with_attachment

def send_email_view(request): 
    send_mail_with_attachment(
        subject="Shift Allocated Table",
        message="Please find the allocated shifts attached.",
        file_path = "C:\\django\\SAS-master\\formatted_shift_scheduletest1.csv",
    )
    return HttpResponse("Email sent successfully!")
