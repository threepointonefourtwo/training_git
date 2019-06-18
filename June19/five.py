#!/usr/bin/env python3
def one(func):
	def inner():
		func()
	return inner


def exter():
	print("this function to be called from outside")

exter = one(exter)
exter()

