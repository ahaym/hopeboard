#!/usr/bin/python3.1
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
password = form.getvalue('passcode')
print('Content-type: text/html')
print()

if password == 'm':
 print('<p>success!<p>')
 print('<meta http-equiv="Refresh" content="0;url=/acte1.html" />')
else:
 print('<center><h1><br><br>Login Failed!<br><img border="0" src="/images/noentry01.jpg" alt=""/></h1></center>')
 print('<meta http-equiv="Refresh" content="3;url=/" />')
