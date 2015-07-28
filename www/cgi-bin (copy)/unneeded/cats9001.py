#!/usr/bin/python
import cgitb
import cgi
cgitb.enable()
form = cgi.FieldStorage()
print 'Content-type: text/html'
print 

print '<title>CGI 101</title>'
print '<h1>A First CGI Example</h1>'
print '<P>Hello, Cats31</p>'
if form.has_key('bgcolor'):
	bgcolor = form.getvalue("bgcolor")
	print '<body bgcolor="' + bgcolor + '">'
langOld = form.getvalue("Languages")
if form.has_key('Language'):
	langNew = form.getvalue("Language")
	langOld = langOld + "," + langNew 
	print 'your name is ' + (langNew)
print 'Languages: ' + (langOld)	
print '<form name="input" action="cats3.py" method="POST">'
print 'Username: <input type="text" name="Language" />'
print '<input type="hidden" name="Languages" value="' + (langOld) + '">'
print 'BackGround color:<select name="bgcolor">'
print '<option value="Blue">Blue</option>'
print '<option value="Red">Red</option>'
print '<option value="White">White</option>'
print '<option value="Green">Green</option>'
print '</select>'
print '<input type="submit" value="Submit" />'
print '</form>'
	
