#!/usr/bin/python
import sqlite3
import cgitb
import cgi

#db
conn = sqlite3.connect('/var/www/example.db')
c = conn.cursor()
#/db

print ''' <form action="start.py" method="GET">
Password: <input type="text" name="first_name">  <br />
<input type="submit" value="Submit" />
</form>'''
