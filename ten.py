#!/usr/bin/env  python3

import xml.etree.ElementTree as ET

file = input("Enter the name of XML file")
tree = ET.parse(file)

root = tree.getroot()

tag = set()
ke = set()

for element in root.iter():
	tag.add(element.tag)
#	ke.add(str(element.attrib.keys()))	
	
for x in tag:
	print("----{0}".format(x))
