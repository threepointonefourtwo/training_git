#!/usr/bin/env python3

import functools
def first(l):
	return functools.reduce(lambda a,b : False if a == False else b if a[len(a)-1] == b[0] else  True if b == True  else False,l)

if __name__ == "__main__":
	l = ["anshul","lshyham","mabhay"]
	l.append("True")
	print(first(l))
