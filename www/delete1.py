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
<title>Delete Entries</title>
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
<h1> Delete Entries -- Exact Match! </h1><br><br>
<form action="delete2.py" method="post">
First Name: <input type="text" name="firstnames"><br />
Last Name: <input type="text" name="lastnames" /><br>
<br>
<input type="submit" value="Go!" />
</form><br><br><br>"""
print  "</body></html>"

