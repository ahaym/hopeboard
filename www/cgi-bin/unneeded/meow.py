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
print 'What is your name?: <input type="text" name="Language" />'
