import os

f = open('writeWithOpen.txt','w')
f.write('write something')
f.close()

os.system('echo "write something" > writeWithEcho.txt')
