import smtplib
from email.mime.text import MIMEText
import getpass

s = smtplib.SMTP('smtp.yeah.net')
s.login('jason_wujiakun@yeah.net',getpass.getpass())
s.set_debuglevel(1)
msg = MIMEText("""body""")
sender = 'jason_wujiakun@yeah.net'
recipients = ['283811824@qq.com','jason_wujiakun@yeah.net']
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
s.sendmail(sender, recipients, msg.as_string())
