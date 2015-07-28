#! /usr/bin/python
import cgi
question = " What is 1 + 1?"
print (question)
answer = raw_input()
answer = int(answer) 
if answer == 2:
     print 'You are right'


else:
     print 'You are wrong'
question2 = " What is 1296 + 1296??"
print (question2)
answer2 = raw_input()
answer2 = int(answer2) 
if answer2 == 2592:
     print 'You are right'


else:
     print 'You are wrong'
