#!/usr/bin/env  python3

from datetime import datetime

#import time

def hi():
	return datetime(1970, 1, 1).strftime('%Y-%d-%B')

print(hi())
