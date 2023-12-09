import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PW = os.environ.get("PW")
SMTP_SERVER = "smtp.gmail.com"
PORT = 465

context = ssl.create_default_context()

rec = "oussama326mejri@gmail.com"
sbj = "GET KITTY'ED ON"
body = "Here\'s your daily dose of kitties"

msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = rec
msg["Subject"] = sbj

msg.attach(MIMEText(body, "plain"))

kitty_path = "cats/kitty.jpg"

with open(kitty_path, "rb") as pic:
    part_pic = MIMEBase("application", "octet-stream")
    part_pic.set_payload(pic.read())

encoders.encode_base64(part_pic)
part_pic.add_header(
    "Content-Disposition",
    f"attachment; filename= {kitty_path}"
)

msg.attach(part_pic)
text = msg.as_string()

with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
    server.login(EMAIL, PW)
    server.sendmail(EMAIL, rec, text)
    print("EMAIL SENT!")