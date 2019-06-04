#!/usr/bin/env python3

import json

file = input("Enter the name of json file")
with open(file,"r") as ff:
	data = json.load(ff)

#print(type(data))

for a,b in data.items():
	if type(b) == str:
		data.update({a:""})
	elif type(b) == int:
		data.update({a:0})
	elif type(b) == list:
		data.update({a:[]})

print(data)
