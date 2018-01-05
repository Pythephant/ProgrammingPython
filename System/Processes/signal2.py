import signal, time, sys
def now():
	return time.ctime(time.time())

def onSignal(signum, stackframe):
	print('Got alarm',signum,'at',now(),stackframe)

if __name__ == '__main__':
	while True:
		print('Setting at', now())
		signal.signal(signal.SIGALRM, onSignal)
		signal.alarm(5)
		signal.pause()
