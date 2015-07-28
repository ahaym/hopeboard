#!/usr/bin/python
import sqlite3
import cgitb
import cgi
import datetime
import geopy
from  geopy import geocoders
cgitb.enable()
g = geocoders.Google()
place, (lat, lng) = g.geocode("1202 Timberland Drive 35603")  
template = """<!DOCTYPE html>
<html>
  <head>
    <title>Maps</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="UTF-8">
    <link href="maps.css"
        rel="stylesheet" type="text/css">
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
  <body>
    <div id="map_canvas"></div>
  </body>
</html>"""
print template % (lat, lng)
