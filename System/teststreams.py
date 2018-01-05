def interact():
	print('Hello stream world!')
	while True:
		try:
			reply = input('Enter a number:')
		except EOFError:
			break
		else:
			num = float(reply)
			print('%f squared is %f' % (num, num**2))
	print('Bye')

if __name__ == '__main__':
	interact()
