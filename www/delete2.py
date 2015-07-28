#!/usr/bin/python
import sqlite3
import cgitb
import cgi
import datetime

#cgitb.enable()

form = cgi.FieldStorage()
print "Content-type: text/html\n\n\n"

print """<html>
<head>
<title>Entries Deleted.</title>
</head>
<body>
<h1> Entries Deleted. </h1>"""
firstname = form.getvalue('firstnames')
lastname = form.getvalue('lastnames')
#firstname = 'jon'
#lastname = 'ron'

conn = sqlite3.connect('/var/www/example.db')
c = conn.cursor()
c.execute("DELETE from hope where firstname = '%s' and lastname = '%s'" % (firstname, lastname))
conn.commit()
c.close()
print '''<meta http-equiv="REFRESH" content="0;url=index.py?first_name=SAND">'''

print  "</body></html>"


