import shelve
from person import Person, Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 32, 40000, 'hardware')
tom = Manager('Tom Due', 27 , 10000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

