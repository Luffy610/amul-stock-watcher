import smtplib
from email.mime.text import MIMEText
import os

def send_email_notification(subject, body, email_recipient):
    try:
        # Email configuration
        smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('SMTP_PORT', 587))
        email_sender = os.getenv('GMAIL_USER')
        email_password = os.getenv('GMAIL_PASSWORD')
        if email_sender is None or email_password is None:
            raise ValueError("Email configuration is not set properly in environment variables.")

        # Create the email content
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = email_sender
        email_recipient = [email.strip() for email in email_recipient.split(",")]
        msg['To'] = ", ".join(email_recipient)

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(email_sender, email_password)
            server.send_message(msg)
        print(f"Email sent successfully to {email_recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")