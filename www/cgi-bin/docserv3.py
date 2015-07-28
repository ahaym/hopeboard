#!/usr/bin/python
import cgitb
import cgi
import sqlite3

import smtplib
import geopy
from  geopy import geocoders
cgitb.enable()
g = geocoders.Google()
form = cgi.FieldStorage()
conn = sqlite3.connect('/var/www/cgi-bin/example')
conn.row_factory = sqlite3.Row
trackid = form.getvalue("trackid")
rdx = form.getvalue("none")
c = conn.cursor()
c.execute("select * from peopletracker where trackid = '"+ trackid + "'").fetchone
for row in c:
 place, (lat, lng) = g.geocode(row["Address"] + " " + row["ZIP"])

print '<!DOCTYPE html>'
print '''<html><head>
<link href="actepatlist.css"
        rel="stylesheet" type="text/css"><meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="UTF-8">
<script type="text/javascript"
        src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>
    <script type="text/javascript">
      function initialize() {
        var myOptions = {
          zoom: 4,
          center: new google.maps.LatLng(%s, %s),
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById('map_canvas'),
            myOptions);

        var marker = new google.maps.Marker({
          position: map.getCenter(),
          map: map,
          title: 'Click to zoom'
        });

        google.maps.event.addListener(map, 'center_changed', function() {
          // 3 seconds after the center of the map has changed, pan back to the
          // marker.
          window.setTimeout(function() {
            map.panTo(marker.getPosition());
          }, 3000);
        });

        google.maps.event.addListener(marker, 'click', function() {
          map.setZoom(8);
          map.setCenter(marker.getPosition());
        });
      }

      google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
<body>''' % (lat, lng)


print '<h1><p>Victims Profile</p></h1>'


    

vname = ''
vgender = ''
if trackid is None:
	print '<h1>Error, no trackid!</h1>'
else:

	c = conn.cursor()
	c.execute("select * from peopletracker where trackid = '"+ trackid + "'").fetchone

	
	
	tableContent = ''
	tableFooter = '</table>'
	tableHdr = '<table id="patients">'
	tableHdr = tableHdr + '<tr>'
	tableHdr = tableHdr + '<th>Name</th>'
	tableHdr = tableHdr +  '<th style="text-align:center">Age</th>'
	tableHdr = tableHdr +  '<th style="text-align:center">Gender</th>'
	tableHdr = tableHdr +  '</tr>'

	for row in c:
	 print '<H5>Search Status: <font size="6" face="arial" color="red"> ' + row["Status"] + '</font>'
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
	 print '<h1>Sorry! No records found!</h1>'
	else:
  
	 print tableHdr
	 print tableContent
	 print tableFooter
	 print '<img border="0" src="/images/' + row["imgptr"] + '" align="top"/>&nbsp;&nbsp;'
	 print '<H5>Calamity Info: <font size="3" face="arial" color="red">' + row["DisasterID"] + '</font>'
	 print '<br>Information source: <font size="3" face="arial" color="red">' + row["DisasterName"] + '</font>'
	 print '<br>Source Contact: <font size="3" face="arial" color="red">' + row["agentcontactinfo"] + '</font>'
	 print '<br>Source Agent ID: <font size="3" face="arial" color="red">' + row["agentID"] + '</font>'
	 print '<br>Source Person:<font size="3" face="arial" color="red">' + row["agentname"] + '</font>'
	 print '<br>Source Message: <br><font size="3" face="arial" color="red">' + row["agentnote"] + '</font>'
	 print '''<object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" codebase="http://www.apple.com/qtactivex/qtplugin.cab" height="256" width="320">

<param name="src" value="%s">
<param name="autoplay" value="true">
<param name="type" value="video/quicktime" height="240" width="320">

<embed src="%s" height="240" width="320" autoplay="true" type="video/quicktime" pluginspage="http://www.apple.com/quicktime/download/">

</object>

 ''' % (row["video"], row["video"])
	 if row["searchername"] != "":
	  print '<hr>'
	  print '<br>Searcher Name: <font size="3" face="arial" color="red">' + row["searchername"] + '</font>'
	  print '<br>Searcher Contact Info: <font size="3" face="arial" color="red">' + row["searchercontactinfo"] + '</font>'
	  print '<br>Searcher Message: <br><font size="3" face="arial" color="red">' + row["searchernote"]+ '</font>'

          
           
c.close()
print '''<div id="map_canvas"></div></body></html>'''


	
	
	
