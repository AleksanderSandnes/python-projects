import smtplib, ssl

# For starttls
port = 587
smtp_server = "smtp.gmail.com"
sender_email = "sandnespython@gmail.com"
receiver_email = "lotte.helland@hotmail.com"
password = input("Enter your password: ")
message = """\
Subject: Juhuuu

Denne meldingen ble sendt fra Python."""

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    # Can be omitted
    server.ehlo()
    # Secure the connection
    server.starttls(context=context) 
    #Can be omitted
    server.ehlo()
    server.login(sender_email, password)
    # Send the email
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()