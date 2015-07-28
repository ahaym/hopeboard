#!/usr/bin/python
import cgitb
import cgi
cgitb.enable()
print 'Content-type: text/html'
print 
print '<title>CGI 101</title>'
print '<h1>A First CGI Example</h1>'
print '<P>Hello, Cats</p>'
print '<form name="input" action="cats3.py" method="get">'
print '<h1>Languages: English<h1>'
print 'What is your name?: <input type="text" name="Language" />'
print '<input type="hidden" name="name" value="">'
print 'BackGround color:<select name="bgcolor">'
print '<option value="Blue">Blue</option>'
print '<option value="Red">Red</option>'
print '<option value="White">White</option>'
print '<option value="Green">Green</option>'
print '</select>'
print '<input type="submit" value="Submit" />'
print '</form>'

