#!/usr/bin/python
import sqlite3
import cgitb
import cgi
import datetime

cgitb.enable()

form = cgi.FieldStorage()
print "Content-type: text/html\n\n\n"

print """<html>
<head>
<title>Hello - Second CGI Program</title>
<link type="text/css" rel="stylesheet" href="style.css">
</head>
<body>
<ul>
<li><a href="start.py?first_name=SAND">Home</a></li>
<li><a href="edit.py">Edit</a></li>
<li><a href="add.py">Add</a></li>
<li><a href="delete1.py">Delete</a></li>
<li><a href="search.py">Search</a></li>
<li><a href="upload.py">Upload</a></li>
</ul><br><br>
<h1> Viewing All Entries </h1>"""

conn = sqlite3.connect('/var/www/example.db')
c = conn.cursor()
c.execute("select * from hope where state = 'missing'")

template = """First Name: %s<br>
Last Name: %s<br>
Former Address: %s<br>
Age: %s<br><br>
<img src="%s" /><br><br>
Date: %s<br> %s <br>
id: %s<br>
condition: %s<br>
phone: %s<br><br>
"""

for row in c.fetchall():
    print template % row

print  "</body></html>"


