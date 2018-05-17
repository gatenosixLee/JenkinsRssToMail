from jinja2 import Template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

me = 'gatenosix@gmail.com'
you = 'gatenosix@gmail.com'

msg = MIMEMultipart('alternative')
msg['Subject'] = 'test'
msg['From'] = me
msg['To'] = you

text = 'test message'

f = open('mailTemplate.html', 'r')
template = Template(f.read())
f.close()

html = template.render(name='asdg')

part2 = MIMEText(html, 'html')

msg.attach(part2)

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(me, 'dlckdqo08907!@#$')

server.send_message(msg)
server.quit()
