#!/usr/bin/python
import sqlite3
import cgitb
import cgi
import datetime

cgitb.enable()
template = "a"

form = cgi.FieldStorage()
print "Content-type: text/html\n\n\n"

print """<html>
<head>
<title>Showing All Entries</title>
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
lastname = form.getvalue('lastnames')
firstname = form.getvalue('firstnames')
conn = sqlite3.connect('/var/www/example.db')
c = conn.cursor()
c.execute("select * from hope where lastname = '%s' AND firstname = '%s'" % (lastname, firstname)
temp = '''First Name: %s<br>
Last Name: %s<br>
Former Address: %s<br>
Age: %s<br><br>
<img src="images/%s" /><br><br>
Date: %s<br> %s <br>
id: %s<br>
condition: %s<br>
phone: %s<br><br>
<hr /><br><br>'''

template2 = """First Name: %s<br>
Last Name: %s<br>
Former Address: %s<br>
Age: %s<br><br>
<!-- Codes by Quackit.com -->
<script type="text/javascript">
// Popup window code
function newPopup(url) {
	popupWindow = window.open(
		url,'popUpWindow','height=700,width=800,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
}
</script>
<a href="JavaScript:newPopup('http://www.quackit.com/html/html_help.cfm');">Open a popup window</a>
<br><br>
Date: %s<br> %s <br>
id: %s<br>
condition: %s<br>
phone: %s<br><br>
<hr /><br><br>
"""

for row in c.fetchall():
 if os.path.exists('/var/www/images/' + row[8]):
    print template % (row[0], row[1], row[2], row[3], row[7], row[5], row[6], row[7], row[8], row[9])
 else:
  print template2 % (row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[9])
    

print  "</body></html>"

<script type="text/javascript">
// Popup window code
function newPopup(url) {
	popupWindow = window.open(
		url,'popUpWindow','height=700,width=800,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
}
</script>
<a href="JavaScript:newPopup('http://www.quackit.com/html/html_help.cfm');">Open a popup window</a>



