import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()


def send_email(jobs):

    if not jobs:
        print("No new jobs found. Email not sent.")
        return

    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    subject = f"🟢 {len(jobs)} New Job(s) Found"

    body = ""

    for job in jobs:

        body += f"""
============================================================

Title       : {job.title}
Company     : {job.company}
Posted Date : {job.posted_date}
Location    : {job.location}
Source      : {job.source}

Apply Here:
{job.link}

============================================================

"""

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, sender_password)

        server.send_message(message)

        server.quit()

        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Failed to send email.")
        print(e)