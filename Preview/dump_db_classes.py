import shelve

db = shelve.open('class-shelve')
for key in db:
	print(db[key])

