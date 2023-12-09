import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PW = os.environ.get("PW")
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

context = ssl.create_default_context()

with smtplib.SMTP(SMTP_SERVER, PORT) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(EMAIL, PW)

    rec = "oussama326mejri@gmail.com"
    msg = """Subject: GET REKT
    \n
    \n    
    yo what's up
    """

    server.sendmailen(EMAIL, rec, msg)