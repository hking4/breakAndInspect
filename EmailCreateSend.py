## createEmail(body)
## Connects to GMAIL SMTP and send email to required addresses
## takes one argument for the entire email body
def send(body):
    import smtplib, ssl
    import getpass
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import datetime as dt
    #import EmailPassDec as dec
    import PWdecr as pw

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "break.inspect@gmail.com"
    receiver_email = "tyler.dugan@rocketmail.com"
    ts = dt.datetime.now()
    #password = dec.getPW()
    password = pw.getPW('.\emailPW.bin')
    message = """\
    Subject: Violation Log\n
    {}.""".format(body)


    bettermessage = MIMEMultipart()
    bettermessage['From'] = 'break.inspect@gmail.com'
    bettermessage['To'] = 'tyler.dugan@rocketmail.com'
    bettermessage['Subject'] = 'Violation log for ' + getpass.getuser() + ' generated on ' + str(ts)

    bettermessage.attach(MIMEText(body, 'plain'))
    
    try:
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(sender_email, password)
        s.send_message(bettermessage)
        print('connected')
    except:
        print('Exception')

    # try:
    #     context = ssl.create_default_context()
    #     with smtplib.SMTP(smtp_server, port) as server:
    #         server.ehlo()  
    #         server.starttls(context=context)
    #         server.ehlo()  
    #         server.login(sender_email, password)
    #         #server.sendmail(sender_email, receiver_email, message)
    #         server.sendmail(sender_email, receiver_email, bettermessage)
    #         print('Email Sent')
    # except:
    #     print('Exception...email not sent')