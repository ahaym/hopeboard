#!/usr/bin/python
import cgitb
import cgi 
import sqlite3
import smtplib
import datetime
cgitb.enable()
form = cgi.FieldStorage()
conn = sqlite3.connect('/var/www/cgi-bin/example') #imports pakages and connects to the database
conn.row_factory = sqlite3.Row  
noEntry = True



print 'Content-type: text/html'
print ''
print '<link type="text/css" rel="stylesheet" href="actepatlist.css">'
print '<h1><p>Registered Area Victims</p></h1>'
lname = form.getvalue("lname")
fname = form.getvalue("fname")
Phno = form.getvalue("phno")
if lname is None: #Detects if fields are empty
 lname = ""
else:
 noEntry = False
if fname is None:
 fname = "" 
else:
 noEntry = False
if Phno is None:
 Phno = "" 
else:
 noEntry = False

if noEntry :
 print '<h1>You need to enter name!</h1>'
else:

 c = conn.cursor()

 c.execute("select * from peopletracker where lastname like '"+ lname + "%' and firstname like '"+ fname +"%'")
 tableContent = ''
 mailtxt = ''
 tableContentfooter = '</table>'
 tableContentHdr = '<table id="patients">'
 tableContentHdr = tableContentHdr + '<tr>'
 tableContentHdr = tableContentHdr + '<th>Name</th>'
 tableContentHdr = tableContentHdr +  '<th style="text-align:center">Age</th>'
 tableContentHdr = tableContentHdr +  '<th style="text-align:center">Gender</th>'
 tableContentHdr = tableContentHdr +  '<th style="text-align:center">Status</th>'
 tableContentHdr = tableContentHdr +  '<th style="text-align:center">Disaster Name</th>'
 tableContentHdr = tableContentHdr +  '</tr>' # Generates the Web Page with the information about the selected person
 femalecnt = 0
 malecnt = 0
for row in c:
 tableContent = tableContent + '<tr class="alt">'
 tableContent = tableContent + '<td><a href="/cgi-bin/docserv3.py?trackid=' + row["trackid"] +'" target="rtFrame" style="text-decoration : none">'
 tableContent = tableContent + '<img border="0" src="/images/' + row["imgptr"] + '" width="50" height="50" align="bottom"/>&nbsp;&nbsp;' + row["lastname"] + ', ' + row["firstname"] + '</td>'
 tableContent = tableContent + '<td style="text-align:center">' + row["age"] + ' </td>'
 tableContent = tableContent + '<td style="text-align:center">' + row["sex"] + ' </td>'
 tableContent = tableContent + '<td style="text-align:center">' + row["status"] + ' </td>'
 tableContent = tableContent + '<td style="text-align:center">' + row["Disastername"] + ' </td>'
 tableContent = tableContent + '</tr>'
 tableContent = tableContent + '<tr>'
 print ''

if tableContent == '':
 print '<h1>Sorry! No records found!</h1>'
else:
#email
 def prompt(prompt):
  return raw_input(prompt).strip() #Unused Email & SMS script
 
print tableContentHdr
print tableContent
print tableContentfooter
#sendmailsms(mailtxt)

c.close()
