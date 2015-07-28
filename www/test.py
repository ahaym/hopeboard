#!/usr/bin/python
import sqlite3
import cgitb
import cgi

#db
conn = sqlite3.connect('/var/www/example.db')
c = conn.cursor()
#/db


# Required header that tells the browser how to render the text.
print "Content-type: text/html\n\n\n"
form = cgi.FieldStorage() 
#Start Getvalues
password = form.getvalue('first_name')
#End Getvalues

#HTML Page Rendering
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
if password == "SAND":
 print ' <a href="add.py" target="_blank">Add Entry</a> '

else:
 print "<h2>Wrong Password</h2>"
print "</body>"
print "</html>"
