#!/usr/bin/python3.1
import cgitb
import cgi
import sqlite3
import smtplib
import geopy
from  geopy import geocoders
cgitb.enable()
form = cgi.FieldStorage()
conn = sqlite3.connect('/var/www/cgi-bin/example')
conn.row_factory = sqlite3.Row

print('Content-type: text/html')
print()
print('<link type="text/css" rel="stylesheet" href="actepatlist.css">')

print('<h1><p>Victims Profile</p></h1>')

trackid = form.getvalue("trackid")
    

vname = ''
vgender = ''
if trackid is None:
	print('<h1>Error, no trackid!</h1>')
else:

	c = conn.cursor()
	c.execute("select * from peopletracker where trackid = '"+ trackid + "'")

	place, (lat, lng) = g.geocode(row["Address"])
	
	tableContent = ''
	tableFooter = '</table>'
	tableHdr = '<table id="patients">'
	tableHdr = tableHdr + '<tr>'
	tableHdr = tableHdr + '<th>Name</th>'
	tableHdr = tableHdr +  '<th style="text-align:center">Age</th>'
	tableHdr = tableHdr +  '<th style="text-align:center">Gender</th>'
	tableHdr = tableHdr +  '</tr>'

	for row in c:
	 print('<H5>Search Status: <font size="6" face="arial" color="red"> ' + row["Status"] + '</font>') 
	 tableContent = tableContent + '<tr class="alt">'
	 tableContent = tableContent + '<td>' + row["lastname"] + ', ' + row["firstname"] + '</td>'
	 if vname == '':
	  vname = row["firstname"] + ' ' + row["lastname"]
	  vgender = row["sex"]
	 if row["imgptr"] == "1m":
	  age = "5"
	 else:
	  age = row["age"]
	 tableContent = tableContent + '<td style="text-align:center">' + age + ' </td>'
	 tableContent = tableContent + '<td style="text-align:center">' + row["sex"] + ' </td>'
	 tableContent = tableContent + '</tr>'
	 tableContent = tableContent + '<tr>'
	if tableContent == '':
	 print('<h1>Sorry! No records found!</h1>')
	else:
  
	 print(tableHdr)
	 print(tableContent)
	 print(tableFooter)
	 print('<img border="0" src="/images/' + row["imgptr"] + '" align="top"/>&nbsp;&nbsp;')
	 print('<H5>Calamity Info: <font size="3" face="arial" color="red">' + row["DisasterID"] + '</font>')
	 print('<br>Information source: <font size="3" face="arial" color="red">' + row["DisasterName"] + '</font>')
	 print('<br>Source Contact: <font size="3" face="arial" color="red">' + row["agentcontactinfo"] + '</font>')
	 print('<br>Source Agent ID: <font size="3" face="arial" color="red">' + row["agentID"] + '</font>')
	 print('<br>Source Person:<font size="3" face="arial" color="red">' + row["agentname"] + '</font>')
	 print('<br>Source Message: <br><font size="3" face="arial" color="red">' + row["agentnote"] + '</font>')
	 if row["searchername"] != "":
	  print('<hr>')
	  print('<br>Searcher Name: <font size="3" face="arial" color="red">' + row["searchername"] + '</font>')
	  print('<br>Searcher Contact Info: <font size="3" face="arial" color="red">' + row["searchercontactinfo"] + '</font>')
	  print('<br>Searcher Message: <br><font size="3" face="arial" color="red">' + row["searchernote"]+ '</font>')
	c.close()


	
	
	
