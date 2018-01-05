import signal, time, sys
def now():
	return time.ctime(time.time())

def onSignal(signum, stackframe):
	print('Got signal',signum,'at',now(),stackframe)

if __name__ == '__main__':
	signum = int(sys.argv[1])
	signal.signal(signum, onSignal)
	while True:
		signal.pause()
