class Person:
	def __init__(self, name, age, pay = 0, job = None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self, percent):
		self.pay += self.pay*percent

	def __str__(self):
		return '%s => %s: %s, %s' % (self.__class__.__name__, self.name, self.job, self.pay)

class Manager(Person):
	def __init__(self, name, age, pay = 0):
		Person.__init__(self, name, age, pay, job = 'manager')

	def giveRaise(self, percent, bonus = 0.1):
		Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
	bob = Person('Bob Smith', 42, 3000, 'software')
	sue = Person('Sue Jones', 45, 4000, 'hardware')
	tom = Manager('Tom Jason', 27, 10000)

	print(tom)
	print(bob.name, sue.pay)
	print(bob.lastName())
	sue.giveRaise(0.1)
	print(sue.pay)
	tom.giveRaise(0.2)
	print(tom)
