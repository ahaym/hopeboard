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
print """<title>Welcome to Hopeboard</title>
"""
print "</head>"
print "<body>"
if password == "SAND":
 print ''' <a href="add.py" target="_blank">Add Entry</a><br><br><a href="delete1.py" target="_blank">Delete Entry</a><br><br><a href="view.py" target="_blank">View All Entries</a></br></br><a href="upload.py" target="_blank">Upload a Picture</a><br><br><a href="search1.py" target="_blank">Search Entries</a><br><br><a href="view2.py" target="_blank">View Missing</a><br><br><a href="view3.py" target="_blank">View Found</a>


 '''

else:
 print "<h2>Wrong Password</h2>"
print "</body>"
print "</html>"
