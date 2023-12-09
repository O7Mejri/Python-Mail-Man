import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PW = os.environ.get("PW")
SMTP_SERVER = "smtp.gmail.com"
PORT = 465  # The default port for this is 465. 
            # Thus, if port is zero, or not specified, .SMTP_SSL() will use this standard port for SMTP over SSL


context = ssl.create_default_context()

with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
    server.login(EMAIL, PW)

    rec = "oussama326mejri@gmail.com"
    msg = """Subject: GET REKT
    \n
    \n    
    yo what's up
    """

    server.sendmailen(EMAIL, rec, msg)