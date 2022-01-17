from dotenv import load_dotenv
import yagmail
import os
import pandas

load_dotenv()

# Create initial variable for the sender.
sender_email = os.getenv("SENDER_EMAIL")

# Email subject.
email_subject = "Hello from Python!"

# Create an SMTP object instance (login to gmail).
smtp = yagmail.SMTP(user=sender_email, password=os.getenv("APP_PASSWORD"))

# Read the .csv file content using pandas.
cl = pandas.read_csv("contacts.csv")

for index, row in cl.iterrows():
    # Email body.
    email_body = f"""
    Hello {row["name"]}! 
    This is the body content of the email.
    Best regards,
    The Python Script.
    """
    # Send email.
    smtp.send(to=row["email"], subject=email_subject, contents=email_body)
    print("Email successfully sent!")