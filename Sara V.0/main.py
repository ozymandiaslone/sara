from email import message_from_binary_file
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

msg_content = """
Hi! My name is Sara, and I have been creating professional YouTube thumbnails for over a year now, not to mention years of experience in Photoshop. I would love to 
start working with your channel! I will attatch some files to serve as examples of what to expect. I am available nearly 24/7, and almost always deliver within 24 hours.

Right now, I offer one thumbnail for $10, 2 for $18, and 3 for $24. Of course, I will continue working until you are satisfied with the end product.
If you ever need thumbnails, please don't hesitate to send me an E-mail describing what you need. Thank you!
"""
msg_subject = "Affordable professional thumbnails"
msg_from = "Sara's Thumbnails"
msg_recipients = ["saltsperkins@gmail.com"]

def send_email(msg_content, msg_subject, msg_from, msg_to):
    msg = EmailMessage()
    msg.set_content(msg_content)
    msg['Subject'] = msg_subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    with open('./thumbnails/thumb1.png', 'rb') as f:
        img_data = f.read()
    msg.add_attachment(img_data, maintype='image',subtype='png')
    with open('./thumbnails/thumb2.png', 'rb') as f:
        img_data = f.read()
    msg.add_attachment(img_data, maintype='image',subtype='png')
    with open('./thumbnails/thumb3.jpg', 'rb') as f:
        img_data = f.read()
    msg.add_attachment(img_data, maintype='image',subtype='jpg')
    with open('./thumbnails/thumb4.jpg', 'rb') as f:
        img_data = f.read()
    msg.add_attachment(img_data, maintype='image',subtype='jpg')

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("saraliminal@gmail.com", "Yutan#123")
    server.send_message(msg)
    server.quit()
for i in msg_recipients:
    send_email(msg_content, msg_subject, msg_from, i)