import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class SendEmail:
        gmail_user = 'smartMailAPSU@gmail.com'
        gmail_passwd = '**'
        toAdd = 'smartMailAPSU@gmail.com'
        fromAdd = gmail_user
	
        def __init__(self):
                self.gmail_user = 'smartMailAPSU@gmail.com'
                self.gmail_passwd = '**'
                self.toAdd = 'smartMailAPSU@gmail.com'
                self.fromAdd = self.gmail_user


        def SendEmail(self, filename):
                img_data = open(filename, 'rb').read()
                msg = MIMEMultipart()
                msg['From'] = self.fromAdd
                msg['To'] = self.toAdd
                msg['Subject'] = "You've got mail!!"
                body = "Testing Email"
                msg.attach(MIMEText(body, 'plain'))
                image = MIMEImage(img_data, name = os.path.basename(filename))
                msg.attach(image)

                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(self.gmail_user, self.gmail_passwd)                
                s.sendmail(self.fromAdd, self.toAdd, msg.as_string())
                s.quit()

