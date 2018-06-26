#!/usr/bin/env python

# Application for logging
from time import ctime, sleep 
#print(ctime())

def tsfunc(func):
	def wrappedFunc():
		print ('[%s] %s() called' % (
			ctime(), func.__name__) )
		return func()
	return wrappedFunc

@tsfunc
def foo(): 
	pass
sleep(4) 

for i in range(2):
 sleep(1)
 foo()