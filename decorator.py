#!/usr/bin/env python3.6

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

#ordinary()

pretty = make_pretty(ordinary)
#pretty()


def smart_divide(func):
   def inner(a,b):
      print("I am going to multiply",a,"and",b)
      if b == 0:
         print("Whoops! cannot multiply")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
#print(divide(2,5))
#print(divide(2,0))

#@smart_divide 
def multiply(a,b):
	print (a*b)
#(multiply(2,0))

def add_five(func):
	return func + 5

print(add_five(multiply(5,4)))

