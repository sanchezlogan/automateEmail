import os
import webbrowser, sys, requests, os, requests, bs4
import smtplip
from email.message import EmailMessage

## Send Email Notifications Outlook

def connectAndSend():
    ## Example for Outlook
	smtpObj = smtplib.SMTP('smtp.office365.com', 587)
	print(smtpObj.ehlo())
	print(smtpObj.starttls())
	## Enter Outlook Credintials for email to send notifications
	smtpObj.login('Username', 'Password')
	## Email will be sent from a txt file
	os.chdir('Directory where txt file is')
	fp = open('txt file')
	msg = EmailMessage()
	msg.set_content(fp.read())
	msg['Subject:'] = 'type subject here'
	msg['From'] = 'Sending Email'
	msg['To'] = 'Recieving Email'
	smtpObj.send_message(msg)
	smtpObj.quit()
	fp.close()
