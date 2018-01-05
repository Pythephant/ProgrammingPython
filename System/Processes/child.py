import os
import sys
import time
import random

time.sleep(random.random())
print('In the child:',os.getpid(),sys.argv[1])
