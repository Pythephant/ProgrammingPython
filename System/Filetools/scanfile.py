def scanner(name, function):
	for line in open(name, 'r'):
		function(line)
