import shelve

db = shelve.open('class-shelve')
for key in db:
	print(db[key], id(db[key]))

bob = db['bob']
print(bob)
print(id(bob))
bob.giveRaise(0.2)
print(bob)
