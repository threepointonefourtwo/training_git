#!/usr/bin/env python3

def f(x):
	print (x*2)

def g(x):
	return x**2

def q(f,g):
	return lambda x: f(g(x))

__name__ = input("enter the name of function")

if __name__=="q":
	x = int(input("enter the value of x"))
#	eval("f")(eval("g")(x))
#	f(g(x))
	q(f,g)(x)
