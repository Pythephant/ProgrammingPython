import sys,os
from ftplib import FTP
from getpass import getpass

conn = FTP('127.0.0.1')
conn.login(user=input('user:').strip(),passwd=getpass('Pswd:'))
conn.dir()
conn.cwd('pics')
print('changing dir to ',conn.pwd())
conn.dir()
filename = input('file to download:')
fout = open(filename,'wb')
conn.retrbinary('RETR '+filename, fout.write, 1024)
conn.quit()
fout.close()
