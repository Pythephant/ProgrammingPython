import smtplib
from email.mime.text import MIMEText
import getpass

msg = MIMEText("""body""")
sender = 'jason_wujiakun@yeah.net'
recipients = ['283811824@qq.com','jason_wujiakun@yeah.net']
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
print(msg.as_string())
