#!/usr/bin/python
import cgitb
import cgi
import sqlite3
cgitb.enable()
form = cgi.FieldStorage()
SpyLang = "Russian"
OurSpy = 0
print 'Content-type: text/html'
print
print '<title>CGI 101</title>'
print '<h1>A First CGI Example</h1>'
langOld = form.getvalue("Languages")
if form.has_key('bgcolor'):
		bgcolor = form.getvalue("bgcolor")
		print '<body bgcolor="' + bgcolor + '">'
if form.has_key('Language'):
	langNew = form.getvalue("Language")
	if langNew == SpyLang:
		OurSpy = 1
	langOld = langOld + "," + langNew 
	
if OurSpy == 1:
	print '<h1> Welcome comrade! </h1>'
	print '<form name="input" action="spycats1.py" method="POST">'
	print 'Enter your secret code: <input type="password" name="Language" />'
	print '<input type="hidden" name="Languages" value="' + (langOld) + '">'
	print '<input type="submit" value="Submit" />'
	print '</form>'	
else:
	print '<P>Hello, Cats31</p>'
	print 'You also speak ' + (langNew)
	print 'Languages: ' + (langOld)	
	print '<form name="input" action="cats3.py" method="POST">'
	print 'Username: <input type="Text" name="Language" />'
	print '<input type="hidden" name="Languages" value="' + (langOld) + '">'
	print 'BackGround color:<select name="bgcolor">'
	print '<option value="Blue">Blue</option>'
	print '<option value="Red">Red</option>'
	print '<option value="White">White</option>'
	print '<option value="Green">Green</option>'
	print '</select>'
	print '<input type="submit" value="Submit" />'
	print '</form>'
	
