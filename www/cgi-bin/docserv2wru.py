#!/usr/bin/python3.1 
import cgitb
import cgi 
import sqlite3
import smtplib
cgitb.enable()
form = cgi.FieldStorage()
conn = sqlite3.connect('/var/www/cgi-bin/example') #imports pakages and connects to the database
conn.row_factory = sqlite3.Row





print 'Content-type: text/html'
print ''
print '<link type="text/css" rel="stylesheet" href="actepatlist.css">'
print '<h1><p>Missing loved Ones</p></h1>'

c = conn.cursor()

c.execute("select * from peopletracker where status = 'Missing'")

tableContent = ''
mailtxt = ''
tableContentfooter = '</table>'
tableContentHdr = '<table id="patients">'
tableContentHdr = tableContentHdr + '<tr>'
tableContentHdr = tableContentHdr + '<th>Name</th>'
tableContentHdr = tableContentHdr +  '<th style="text-align:center">Age</th>'
tableContentHdr = tableContentHdr +  '<th style="text-align:center">Gender</th>'
tableContentHdr = tableContentHdr +  '<th style="text-align:center">Status</th>'
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
 tableContent = tableContent + '</tr>'
 tableContent = tableContent + '<tr>'

if tableContent == '':
 print('<h1>Sorry! No records found!</h1>')
else:
 print tableContentHdr
 print tableContent
 print tableContentfooter

c.close()


	
	
	
