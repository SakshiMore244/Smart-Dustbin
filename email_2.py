import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "raspi.iot33@gmail.com"
my_password = r"raspberryPi33"
you = "sakshimore244@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Hello"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Hello. This is sent from RPi.</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)

# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
s = smtplib.SMTP_SSL('smtp.gmail.com')
# uncomment if interested in the actual smtp conversation
# s.set_debuglevel(1)
# do the smtp auth; sends ehlo if it hasn't been sent already
s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()
