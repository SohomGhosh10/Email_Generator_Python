import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(to, subject, body):
    from_email = 'sohomghosh06@gmail.com'
    from_password = 'stft bumj stli wazg'
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to, msg.as_string())
        server.close()
        print("Email has been sent!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication error. Please check your email and app password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Sorry, email not sent.")

if __name__ == "__main__":
    try:
        to = input("Whom to send the email? \n")
        subject = input("Subject of the email? \n")
        body = input("Type your text \n")
        sendEmail(to, subject, body)
    except Exception as e:
        print(f"An error occurred: {e}")
