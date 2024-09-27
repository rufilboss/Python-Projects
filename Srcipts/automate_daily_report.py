import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime

# Email Setup
EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP server
EMAIL_PORT = 587  # Port for TLS
SENDER_EMAIL = 'example@gmail.com'
SENDER_PASSWORD = 'Example123'
RECEIVER_EMAIL = 'user@example.com'

# Prepare the email content
def create_email(subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    
    # Add body to email
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach a file if provided
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(part)
    
    return msg

# Send the email
def send_email(subject, body, attachment_path=None):
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # Create and send email
        msg = create_email(subject, body, attachment_path)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"Email sent successfully to {RECEIVER_EMAIL}")
        
        # Close the SMTP connection
        server.quit()
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Automate the email report
def daily_report():
    subject = f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}"
    body = "Hello,\n\nThis is your daily report.\n\nBest regards,\nYour Automation Script"
    
    # Optional: You can add the path to a report (CSV, PDF, etc.)
    attachment_path = 'test.csv'
    
    # Send the email
    send_email(subject, body, attachment_path)

# Schedule the script to run daily
if __name__ == '__main__':
    daily_report()
