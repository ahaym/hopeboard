#!/usr/bin/python
import cgitb
import cgi
import smtplib
cgitb.enable()
print('Content-type: text/html')
print() 
print('<title>CGI 101</title>')
print('<h1>Welcome to Docserv1</h1><br><br><br>')
print('<img src="cat221.gif" alt="meow" /><br><br><br>')
print('<p>Type patient last name or part of last name in space below, then press enter.')
print('<form name="input" action="docserv2.py" method="post">')
print('Patient Last Name:: <input type="text" name="lname" /><br>')
print('Patient First Name:: <input type="text" name="fname" /><br>')
print('<input type="submit" value="Submit" />')
print('</form>')


