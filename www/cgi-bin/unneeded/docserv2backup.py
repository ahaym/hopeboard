#!/usr/bin/python3.1
import cgitb
import cgi
import sqlite3
cgitb.enable()
form = cgi.FieldStorage()
conn = sqlite3.connect('/var/www/cgi-bin/example')
print('Content-type: text/html')
print()
print('<h1>DocServ Patient List</h1>')
lname = form.getvalue("lname")
fname = form.getvalue("fname")
if lname or fname is None:
	print('<h1>You need to enter name!</h1>')
else:
	c = conn.cursor()
	c.execute("select * from patients2 where lastname like '"+ lname + "%' and firstname like '"+ fname +"'")
	
	html = ''
	htmlfooter = '</table>'
	htmlHdr = '<table border="2">'
	htmlHdr = htmlHdr + '<tr>'
	htmlHdr = htmlHdr + '<td>---Patient Name---</td>'
	htmlHdr = htmlHdr +  '<td style="text-align:center">---DOB---</td>'
	htmlHdr = htmlHdr +  '<td style="text-align:center">Gender</td>'
	htmlHdr = htmlHdr +  '</tr>'

	#print '<P> Patient Name          DOB        Gender     </p> <hr>'
	for row in c:
	# print '<tr>'
	# print '<td>' + row[1] + ', ' + row[2] + '</td>'
	# print '<td style="text-align:right">' + row[3] + ' </td>'
	# print '<td style="text-align:center">' + row[4] + ' </td>'
	# print '</tr>'
	# print '<tr>'
	 html = html + '<tr>'
	 html = html + '<td>' + row[1] + ', ' + row[2] + '</td>'
	 html = html + '<td style="text-align:right">' + row[3] + ' </td>'
	 html = html + '<td style="text-align:center">' + row[4] + ' </td>'
	 html = html + '</tr>'
	 html = html + '<tr>'
	 #print '<P>'+ row[1] + ', ' + row[2] + ' DOB: ' + row[3] + ' Gender: ' + row[4] +'</p>'
	#html = html + '</table>'
	if html == '':
	 print('<h1>Sorry! No records found!</h1>')
	else:
	 print(htmlHdr)
	 print(html)
	 print(htmlfooter)

	c.close()


	
	
	
