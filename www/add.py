#!/usr/bin/python
import sqlite3
import cgitb
import cgi
import datetime
import os, sys

print '''<html><head><link type="text/css" rel="stylesheet" href="style.css"></head><body><ul>
<li><a href="start.py?first_name=SAND">Home</a></li>
<li><a href="edit.py">Edit</a></li>
<li><a href="add.py">Add</a></li>
<li><a href="delete1.py">Delete</a></li>
<li><a href="search.py">Search</a></li>
<li><a href="upload.py">Upload</a></li>
</ul><br><br><h1> ADD ENTRIES</h1>'''

#db
conn = sqlite3.connect('/var/www/example.db')
c = conn.cursor()
#/db


# Required header that tells the browser how to render the text.
form = cgi.FieldStorage() 
#No getvalues here! No one expects the Spanish Inquisition fus roh dah foobar!
print '''<form action="add2.py" method="post">
First Name: <input type="text" name="firstname"><br />
Last Name: <input type="text" name="lastname" /><br>
Age(Type a number!): <input type="text" name="age"<br><br>
Former Address: <input type="text" name="formeraddr"><br>
Url of Uploaded Picture:<input type="text" name="picture"><br>
Condition:<select name="condition">
  <option value="missing">Missing</option>
  <option value="found">Found</option>
</select> <br>
Phone Number to Contact: <input type="text" name="phone"><br>
Everything Else (Accepts html format!):<br>
<textarea name="other" cols="50" rows="4"></textarea>
<br><br>


<input type="submit" value="Submit" />
</form></html>'''



