## createEmail(body)
## Connects to GMAIL SMTP and send email to required addresses
## takes one argument for the entire email body
def send(body):
    import smtplib, ssl
    #import EmailPassDec as dec
    import PWdecr as pw

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "break.inspect@gmail.com"
    receiver_email = "tyler.dugan@rocketmail.com"
    #password = dec.getPW()
    password = pw.getPW('.\emailPW.bin')
    message = """\
    Subject: Violation Log\n

    {}.""".format(body)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo()  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)