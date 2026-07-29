import smtplib,os
from email.message import EmailMessage

def send_notification(subject, body, to_email,logFileName):
    # Define your configuration variables
    sender_email = "emptymindd99@gmail.com"
    app_password = "kshr bmxk xtds ciqz"  # Spaces are ignored automatically
    
    # Structure the email data
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email
    msg.set_content(body)
    with open(logFileName, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="plain",
            filename=os.path.basename(logFileName)
        )
    try:
        # Establish connection with Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the traffic connection with TLS encryption
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("Notification sent successfully!")
            
    except Exception as e:
        print(f"Failed to send email. Error: {e}")