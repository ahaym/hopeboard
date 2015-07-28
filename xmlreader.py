#!/usr/bin/python
import sys
import elementtree
from elementtree.ElementTree import Element, SubElement, dump, parse
import getopt
filetoparse = str(sys.argv[1])
parsename = filetoparse.strip('.xml') + '_list.xml'
f = open(parsename, 'w+')
tree = parse(filetoparse)
root = tree.getroot()
furniturelist = {}
#furniturelist['list'] = {}
for child in root:
	child.tag = child.tag
	if child.tag == "lastname":
		lastname = child.text
	elif child.tag == "firstname":
		firstname = child.text
	elif child.tag.startswith("f_"):
		furniturename = child.tag.replace('f_', '')
		furniturename = furniturename
		furniturelist[furniturename] = child.text	
f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<fields>")
names = '<firstname>' + firstname + '</firstname>\n<lastname>' + lastname + '</lastname>\n'
f.write(names) 
#print 
#print lastname, ",", firstname
#print "  Furniture Ordered: "
counter = 0
for key in furniturelist:
	i = str(counter)
	a = str(key)
	a = a.replace('_', ' ')
	print '    ', key, ':', furniturelist[key]
	filetoprint = '<item' + i + '>'
	filetoprint2 = a + '</item' + i + '>\n'
	filetoprint3 = '<qty' + i + '>' + str(furniturelist[key]) + '</qty' + i + '>\n'
	f.write(filetoprint)
	f.write(filetoprint2)
	#print >>f, a
	f.write(filetoprint3)
	counter = counter + 1		
f.write('</fields>')
f.close()		
		

	

