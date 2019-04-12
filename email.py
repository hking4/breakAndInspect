#!/usr/bin/python

import smtplib
import datetime

sender = 'breakAndInspect@gmail.com'

receivers = #supervisors

now = datetime.datetime.now()

amPM = "AM"

message = """ From: From Break And Inspect <breakandinspect@gmail.com>
To: To Supervisor of %s <supervisor email>
Subject: Visit to social media site warning

Hello,

This is a message from the Break and Inspect team. We are informing you that employee
with the username %s accessed a social media site on %d %d, %d at %d:%d:%d %s.

We send this message to inform you about any instances where your employees 
access social media. It is up to you on what kind of action should be taken. 

Sincerely, 
The Break and Inspect Team """  %user %user %now.month %now.day %now.year %now.hour % %now.minute %now.second %amPM

try:
	smtpObj: stmplib.STMP('localhost')
	smtpObj.sendMail(sender,receivers,message)
	print("Successfully sent email")
except:
	SMTPException:
	print("Error: unable to send email")