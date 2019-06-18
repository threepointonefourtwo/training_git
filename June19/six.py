#!/usr/bin/env  python3

def qaz(func):
	def wsx(*args):
		func()
		print("this is " + args[0])
	return wsx

@qaz
def edc():
	print("thIS is edc")

edc("anshul")
#qw("Anshul")
