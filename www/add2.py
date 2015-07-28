#!/usr/bin/python
import sqlite3
import cgitb
import cgi
import datetime
cgitb.enable()

form = cgi.FieldStorage()
print "Content-type: text/html\n\n\n"
print "<html>"
print "<head>" 
#Start Getvalues
date = str(datetime.date.today())
firstname = form.getvalue('firstname')
lastname = form.getvalue('lastname')
age = form.getvalue('age')
formeraddr = form.getvalue('formeraddr')
picfile = form.getvalue('picture')
other = form.getvalue('other')
condition = form.getvalue('condition')
phone = form.getvalue('phone')
print type('picture')
print date
#End Getvalues


#db
conn = sqlite3.connect('/var/www/example.db')
c = conn.cursor()

#/db


# Required header that tells the browser how to render the text.


print "</head>"
print "<body>"
print firstname
print "inserting3..."
#PROBLEM=Unable to open database file
#SOLUTION=Make the readonly database writeable.

c.execute("""insert into hope values (""" +"""'"""+ firstname +"""','""" + lastname +"""','""" + formeraddr +"""','""" + age +"""','""" + picfile +"""','""" + date +"""','""" + other + """', NULL ,'""" + condition + """','""" + phone + """')""")
#c.execute("""insert into test1 values ('Jill', NULL)""")
conn.commit()
c.close()
print "inserting2..."
print '''<meta http-equiv="REFRESH" content="0;url=index.py?first_name=SAND">'''
print "</body>"
print "</html>"
