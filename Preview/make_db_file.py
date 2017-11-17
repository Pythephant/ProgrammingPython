dbfilename = 'peopel-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, filename=dbfilename):
	"formatted dump of database to flat file"
	dbfile = open(filename, 'w')
	for key in db:
		print(key, file = dbfile)
		for (name, value) in db[key].items():
			print(name + RECSEP + repr(value), file = dbfile)
		print(ENDREC, file = dbfile)
	print(ENDDB, file = dbfile)
	dbfile.close()

def loadDbase(filename = dbfilename):
	"parse data from the file to reconstruct the database"
	dbfile = open(dbfilename)
	db = {}
	key = dbfile.readline()
	while key != ENDDB:
		rec = {}
		field = dbfile.readline()
		while field != ENDREC:
			(name, value) = field.split(RECSEP)
			rec[name] = value
			field = dbfile.readline()
		db[key] = rec
		key = dbfile.readline()
	return db


if __name__ == '__main__':
	from initdata import db
	print(db)
	storeDbase(db)
	db2 = loadDbase()
	print(db2)
