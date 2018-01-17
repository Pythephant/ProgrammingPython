import smtplib, sys, email.utils

mailserver = 'smtpout.secureserver.net'

fromAddr = input('From Addr:').strip()
toAddrs = input('To Addrs(split by ;):'.strip().split(';'))
subj = input('Subject:')
date = email.utils.formatdate()

text = 'From: %s\nTo: %s\nData: %s\nSubject: %s\n\n' % (fromAddr, ','.join(toAddrs), date, subj)

print('Type message text, end with line=[Ctrl+d (UNIX), Ctrl+z (Windows)]')
while True:
	line = sys.stdin.readline()
	if not line:
		break
	text += line

print('-'*50)
print(text)
print('-'*50)

print('Connecting SMTP Server...')
server = smtplib.SMTP(mailserver)
isFailed = server.sendmail(fromAddr, toAddrs, text)
server.quit()
if failed:
	print('Failed recipinents:',failed)
else:
	print('No Error.')

