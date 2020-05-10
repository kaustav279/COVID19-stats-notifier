import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def createMail(icases,dcases,pic1,pic2,pic3,state):
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'COVID-19 Stats Update'

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	msgText = MIMEText('This is the alternative plain text message.')
	msgAlternative.attach(msgText)

	msgText = MIMEText("<i>India</i>: <b>{0}</b> cases<br><img src='cid:image1'><br>\n\n<i>{1}</i>: <b>{2}</b> cases<br><img src='cid:image2'><br><br><img src='cid:image3'><br>".format(icases,state,dcases),"html")
	msgAlternative.attach(msgText)

	fp = open(pic1, 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)

	fp = open(pic2, 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID', '<image2>')
	msgRoot.attach(msgImage)

	fp = open(pic3, 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID', '<image3>')
	msgRoot.attach(msgImage)

	return msgRoot

def sendMail(msg,receiver_list):
	sender_email = " " #change to a valid email address,preferably a throwaway account
	password = " " #change to password of the sender email
	msg["From"] = sender_email

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	    server.login(sender_email, password)
	    for receiver_email in receiver_list:
	    	msg["To"] = receiver_email
	    	server.sendmail(sender_email, receiver_email, msg.as_string())
