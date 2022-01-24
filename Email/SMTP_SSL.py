import smtplib, ssl

# Port for SSL
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "sandnespython@gmail.com"
receiver_email = "lotte.helland@hotmail.com"
password = input("Enter your password: ")
message = """\
Subject: Juhuuu

Denne meldingen ble sendt fra Python."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("sandnespython@gmail.com", password)
    # Sending the email
    server.sendmail(sender_email, receiver_email, message)