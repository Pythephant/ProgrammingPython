from socket import *
import time

sock = socket()
sock.connect(('localhost',60000))
f = sock.makefile('w', buffering=1)

print('sending data1')
f.write('1234\n')
f.flush()
time.sleep(5)

print('sending data2')
print('5678',file=f)
f.flush()
time.sleep(5)

print('sending data3')
sock.send(b'9abc\n')

time.sleep(5)
