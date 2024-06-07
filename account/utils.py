import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_email(data):
        # Email configuration (replace with your own)
        email_address = 'atalgpspl.security@geoplanetsolution.in'
        # email_address = os.environ.get('EMAIL_FROM')
        password = 'Security@Gpspl#2023'
        # password =  os.environ.get('EMAIL_PASS')
        smtp_server = 'smtp.hostinger.com'
        smtp_port = 587  # Use 587 with starttls() instead of 465

        # Create a message
        message = MIMEMultipart()
        message['From'] = email_address
        message['To'] = data['to_email']
        message['Subject'] = 'Reset Password AtalGPSPL!'
        securitycode = data['Link']

        # HTML content
        html_content = """
        <html>
        <head></head>
        <body>
          <h1>This is Auto generated mail for reset password security code AttalGPSPL</h1>
          <p> This code is valid till <b style="color: red;">15 min</b>. <i>Copy the below security code</i></p>
          <h3 style="color:#003E58;">Security Code: </h3>
          <h3> <span style="border: 2px solid #003E58; padding: 10px; margin-left: 10px; color: #003E58;">{securitycode}</span> </h3>
        </body>
        </html>
        """.format(securitycode=securitycode)

        # Attach HTML content
        message.attach(MIMEText(html_content, 'html'))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Use starttls() for secure connection

            # Login to the email account
            server.login(email_address, password)

            # Send the email
            server.sendmail(email_address, [data['to_email']], message.as_string())

            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Close the connection in a finally block to ensure it always happens
            if server:
                server.quit()