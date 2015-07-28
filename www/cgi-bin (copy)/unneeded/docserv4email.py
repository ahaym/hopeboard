#!/usr/bin/python3.1
import cgitb
import cgi
import sqlite3
import smtplib
cgitb.enable()
form = cgi.FieldStorage()
conn = sqlite3.connect('/var/www/cgi-bin/example')
noEntry = True
def sendmailsms(msg):
 
	# Add the From: and To: headers at the start!
	 fromaddr = 'DocService'
	 toaddrs  = 'mark32587hay@gmail.com'
	 #msg = 'Subject:DocService \n\n Message:\n' + PatInfo + '\n'

	 server = smtplib.SMTP('localhost')
	 server.set_debuglevel(1)
	 server.sendmail(fromaddr, toaddrs, msg)
	 server.quit()
	 #/email




print('Content-type: text/html')
print()
print('<link type="text/css" rel="stylesheet" href="actepatlist.css">')
print('<P><h2>Your information has been SERVED')
print('<img border="0" src="/images/sms.jpg" width="50" height="50" align="middle"/>.')
chart = form.getvalue("chart")
if chart is None:
	print('<h1>Error, no chart#!</h1>')
else:

	c = conn.cursor()
	c.execute("select * from patients2 where chart = '"+ chart + "'")
	
	tableContent = ''
	mailtxt = ''
	tableContentfooter = '</table>'
	tableContentHdr = '<table id="patients">'
	tableContentHdr = tableContentHdr + '<tr>'
	tableContentHdr = tableContentHdr + '<th>Patient Name</th>'
	tableContentHdr = tableContentHdr +  '<th style="text-align:center">DOB</th>'
	tableContentHdr = tableContentHdr +  '<th style="text-align:center">Gender</th>'
	tableContentHdr = tableContentHdr +  '</tr>'

	for row in c:

	
	 mailtxt = mailtxt +  'Subject: Patient: ' + row[1] + ', ' + row[2] + '\n\n\nDOB: ' + row[3] + '\nGender: ' + row[4] +'\nPhone: 205-533-7238\nPharmacies: http://97.82.17.122'
	 tableContent = tableContent + '<tr class="alt">'
	 tableContent = tableContent + '<td>' + row[1] + ', ' + row[2] + '</td>'
	 tableContent = tableContent + '<td style="text-align:center">' + row[3] + ' </td>'
	 tableContent = tableContent + '<td style="text-align:center">' + row[4] + ' </td>'
	 tableContent = tableContent + '</tr>'
	 tableContent = tableContent + '<tr>'

	if tableContent == '':
	 print('<h1>Sorry! No records found!</h1>')
	else:
	  
	 print(tableContentHdr)
	 print(tableContent)
	 print(tableContentfooter)
	 sendmailsms(mailtxt)
	 print('<br><center><h2>Thank you and have a nice day!<br>Your information has been sent.<h2></center>')

	c.close()


	
	
	
