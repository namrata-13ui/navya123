import smtplib
from email.message import EmailMessage
import os

sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_APP_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")

if not sender_email or not app_password or not receiver_email:
    print("Please set EMAIL_ADDRESS, EMAIL_APP_PASSWORD and RECEIVER_EMAIL.")
    exit()

message = EmailMessage()

message["Subject"] = "Python Email Automation"
message["From"] = sender_email
message["To"] = receiver_email

message.set_content(
    "Hello,\n\n"
    "This email was sent automatically using Python.\n\n"
    "Regards,\n"
    "Namrata"
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.send_message(message)

print("Email sent successfully!")