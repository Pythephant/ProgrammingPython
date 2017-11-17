import cgi, os, sys, shelve
import datetime

def genTimeStamp():
	return '++++++++++++%s+++++++++++++'%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


#log = open('log.txt','a')
shelvename = 'class-shelve'
fieldNames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-type: text/html')
sys.path.insert(0, os.getcwd())



#main html template
replyHtml = """
<html>
<title>People Input Form</title>
<body>
<form method=POST action="peoplecgi.py">
	<table>
	<tr><th>key<td><input type=text name=key value="%(key)s">
	$ROWS$
	</table>
	<p>
	<input type=submit value="Fetch", name=action>
	<input type=submit value="Update", name=action>
</form>
</body>
"""

#insert html for data rows at $ROWS$
row = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rows = ''
for fieldName in fieldNames:
	rows += row %((fieldName,)*3)
replyHtml = replyHtml.replace('$ROWS$', rows)

def htmlize(adict):
	new = adict.copy()
	for field in fieldNames:
		value = new[field]
		new[field] = cgi.escape(repr(value))
	return new

def fetchRecord(db, form):
	try:
		key = form['key'].value
		record = db[key]
		fields = record.__dict__
		fields['key'] = key
	except Exception as e:
		fields = dict.fromkeys(fieldNames, '?')
		fields['key'] = 'Missing or invalid key!'
	return fields

def updateRecord(db, form):
	
	if 'key' not in form:
		fields = dict.fromkeys(fieldNames, '?')
		fields['key'] = 'Missing key input!'
	else:
		key = form['key'].value
		if key in db:
			record = db[key]
		else:
			from person import Person
			record = Person(name='?', age='?')
		for field in fieldNames:
			setattr(record, field, eval(form[field].value))
		db[key] = record
		fields = record.__dict__
		fields['key'] = key
	return fields

db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
	fields = fetchRecord(db, form)
elif action == 'Update':
	fields = updateRecord(db, form)
else:
	fields = dict.fromkeys(fieldNames, '?')
	fields['key'] = 'Missing or invalid action!'

db.close()
print(replyHtml % htmlize(fields))
