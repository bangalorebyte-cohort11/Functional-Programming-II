
# Functions as First-Class objects


```python
def hello_world(h):
      def world(w):
              print(h, w)
      return world # returning functions

h = hello_world # assigning
x = h("hello") # assigning

(x("world"))

# storing functions in a list
function_list = [h, x]
print(function_list)
```

    hello world
    [<function hello_world at 0x1128e3730>, <function hello_world.<locals>.world at 0x1128e36a8>]


The main thing we do with our first class objects, is pass them to our FP built-in functions map(), reduce(), and filter(). Each of these functions accepts a function object as its first argument.


```python
# procederal implementation
# Here we are specifying how to do summation
def naive_sum(list):
    s = 0
    for l in list:
        s += l
    return s
naive_sum([1,2,67])
```




    70




```python
# functional implementation with built-in function
sum(list)


# Here we are not a worried as to how the sum function is working under the hood
```




    10



# Map


```python
# using map to apply functions to iterable objects
# the function map, maps functions to the some iterable object

# map() is a function with two arguments: r = map(func, seq)
#It returns an iterable with the elements changed by func

# simple example
str_to_int = (map(int, ["1", "2", "3"]))
print(str_to_int)
print(next(str_to_int))
print(next(str_to_int))
print(next(str_to_int))

# another example 
def add_by_5(i):
    return i + 5
a = map(add_by_5,[1,2,3,4])
next(a)
next(a)
next(a)
next(a)

```

    <map object at 0x10aa7a588>
    1
    2
    3





    9




```python

```


```python
for i in str_to_int:
    print(i)
```


```python
# Map helps reduce looping 
import time
#looping without map
list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def large_exponent_func():
    for i in list_:
        i = i**480
start = time.time()
large_exponent_func()
end = time.time()
print(end-start)

```

    0.00015497207641601562



```python
start_map = time.time()
large_exponent = map(lambda x: x**480,list_)
end_map = time.time()
print(end_map-start_map)
```

    7.390975952148438e-05


# Lambda
Use lambda functions if you want a shortcut to specify functinos in-line. 
The structure lambda arugments:expression

Drawback:
- Only a single expression can be specified which means no other features like multiple if statements, iteration or exception handling can be included. 

Advantages:
- While the lambda function itself has limited use, typically, lambda is used in the context of some other operations like map, reduce, filter. 


```python
# lambda function to get the square of a number

add = lambda x,y: x+y
add(2,3)
add("hello","world")

```




    'helloworld'




```python
#examples with map

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)



```

    102.56



```python
# we can use the lambda expression to make procedural code functional

# procedural code
starting_number = 96

# get the square of the number
square = starting_number ** 2

# increment the number by 1
increment = square + 1

# cube of the number
cube = increment ** 3

# decrease the cube by 1
decrement = cube - 1

# get the final result
result = print(decrement) # output 783012621312
```

    783012621312


## Filter 

The “filter” function operates on a list and returns a subset of that list after applying the filtering rule.

output_list = filter(f, input_list)



```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output_list = map(lambda x: x > 5, my_list)

for i in output_list:
    print(i)
```

    False
    False
    False
    False
    False
    True
    True
    True
    True


## Challenge

Use filter to create list of only leap years in the following list:


```python
year_lst=[1980, 1988, 1990, 1992, 1993, 1998, 2002]
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python
Leap_Years=list(filter(lambda leap_yrs:(leap_yrs%4==0),year_lst))
```


```python
print("Leap years after applying filter: ", Leap_Years)
```

    Leap years after applying filter:  [1980, 1988, 1992]


# Reduce

The “reduce” function will transform a given list into a single value by applying a given function continuously to all the elements. It basically keeps operating on pairs of elements until there are no more elements left. Let’s say we want to find the product of all the elements in a given list:


```python
reduce(lambda a, b: a * b, my_list)
```




    362880




```python
# define a function `call` where you provide the function and the arguments
def call(x, f):
    return f(x)

# define a function that returns the square
square = lambda x : x*x

# define a function that returns the increment
increment = lambda x : x+1

# define a function that returns the cube
cube = lambda x : x*x*x

# define a function that returns the decrement
decrement = lambda x : x-1

# put all the functions in a list in the order that you want to execute them
funcs = [square, increment, cube, decrement]

# bring it all together. Below is the non functional part. 
# in functional programming you separate the functional and the non functional parts.

print(reduce(call, funcs, 96))
```

    783012621312



```python
# Another example of reduce
import time
#procerdural implementation

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

    # Versus


from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

```


```python

```

## Challenge

Using reduce create a function called average() that calculates the simple average of a set of numbers.


```python

```


```python
def average(List):
    return reduce(lambda x,y:x+y,List)/(len(List))


List=range(15)
print(average(List))
```

    7.0



```python
# Zip

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)

```

    {'a': 1, 'b': 2, 'c': 3}


# Iterators


```python
L = [1,2,3]
it = iter(L)
print(type(it))

print(it.__next__())  # same as next(it)

print(next(it))
print(next(it))
next(it)

```

    <class 'list_iterator'>
    1
    2
    3



    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-14-94ae98cd91c1> in <module>()
          7 print(next(it))
          8 print(next(it))
    ----> 9 next(it)
    

    StopIteration: 


A for loop is also an iterator and under the hood is supporte by the iter() function


```python
# Plain for loop
List_1 = ["Kapil","Aakash","Sirisha"]

for name in List_1: 
    print(name)

```

    Kapil
    Aakash
    Sirisha



```python
# for loop implementation via iter() 
fetch = iter(List_1) #if we print(type) --> we have an iterable object
while True:
	try:
		i = fetch.__next__() #iterator method
	except StopIteration:
		break
	print(i)

```

    Kapil
    Aakash
    Sirisha


# Generators

Here is how a generator function differs from a normal function.

- Generator function contains one or more yield statement.
- When called, it returns an object (iterator) but does not start execution immediately.
- Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
- Once the function yields, the function is paused and the control is transferred to the caller.
- Local variables and their states are remembered between successive calls.
- Finally, when the function terminates, StopIteration is raised automatically on further calls.


```python
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
# running it with for loop
#for i in my_gen():
    #print(i)
# running using next where we can pause whenver

a  = my_gen()
next(a)
next(a)
next(a)
next(a)
```

    This is printed first
    This is printed second
    This is printed at last



    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-25-821dfbb461ff> in <module>()
         21 next(a)
         22 next(a)
    ---> 23 next(a)
    

    StopIteration: 



```python
# Here is another example

def countdown(n):
    print("starting to count from",n)
    while n > 0:
        yield n 
        n -=1
    print("done!")
b  = countdown(10)
c  = countdown(10)
next(b)
next(b)
next(b)
next(b)
```

    starting to count from 10





    7



### Discussion

One interesting thing to note in the above example is that, the value of variable n is remembered between each call.

Unlike normal functions, the local variables are not destroyed when the function yields. In normal functions, applying return exits the function and destorys local variables from memory. Furthermore, the generator object can be iterated only once.

To restart the process we need to create another generator object using something like a = my_gen().




```python
# Another example

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

for i in rev_str("hello"):
    print(i)

```

    o
    l
    l
    e
    h



```python

```

## Advantages of Generators

- Memory Efficient: A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill if the number of items in the sequence is very large. Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.




# Generator Expressions 

- Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.
- Same as lambda function creates an anonymous function, generator expression creates an anonymous generator function.
- The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.
- The major difference between a list comprehension and a generator expression is that while list comprehension produces the entire list, generator expression produces one item at a time.
- They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.






```python
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print(("List Comprehension:"))
print([x**2 for x in my_list],'\n')

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print("Generator Expression:")
for i in (x**2 for x in my_list):
    print(i)
    
# we can also use it in conjunction with 
sum(x**2 for x in my_list)
```

    List Comprehension:
    [1, 9, 36, 100] 
    
    Generator Expression:
    1
    9
    36
    100





    146



## Practical example: 

Generators can be used to pipeline a series of operations. This is best illustrated using an example.

Suppose we have a log file from a famous fast food chain. The log file has a column (3rd column) that keeps track of the number of pizza sold every hour and we want to sum it to find the total pizzas sold in 5 years.

Assume everything is in string and numbers that are not available are marked as 'N/A'. A generator implementation of this could be as follows.


```python

with open('sells.xlsx','rb') as file:
    pizza_col = (line[2] for line in file)
    per_hour = (int(x) for x in pizza_col if x!= 'NA')
    print(type(per_hour))
    print(next(per_hour))
    print("Total pizzas sold = ",sum(per_hour))

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-61-0b9d296c74b9> in <module>()
          1 
    ----> 2 with open('sells.xlsx','rb') as file:
          3     pizza_col = (line[2] for line in file)
          4     per_hour = (int(x) for x in pizza_col if x!= 'NA')
          5     print(type(per_hour))


    FileNotFoundError: [Errno 2] No such file or directory: 'sells.xlsx'


## Advantage of functional programming 

A very large percentage of program errors—and the problem that drives programmers to debuggers—occur because variables obtain unexpected values during the course of program execution. Functional programs bypass this particular issue by simply not assigning values to variables at all.

Lets look at this with an example:
The goal here is to print out a list of pairs of numbers whose product is more than 25. The numbers that make up the pairs are themselves taken from two other lists. 


```python
# Nested loop procedural style for finding big products
xs = (1,2,3,4)
ys = (10,15,3,22)
bigmuls = []
# ...more stuff...
for x in xs:
    for y in ys:
        # ...more stuff...
        if x*y > 25:
            bigmuls.append((x,y))
            # ...more stuff...
# ...more stuff...
print(bigmuls)
```

    [(2, 15), (2, 22), (3, 10), (3, 15), (3, 22), (4, 10), (4, 15), (4, 22)]


Discussion : This project is small enough that nothing is likely to go wrong.  But perhaps our goal is embedded in code that accomplishes a number of other goals at the same time. The sections commented with "more stuff" are the places where side-effects are likely to lead to bugs. At any of these points, the variables xs, ys, bigmuls, x, y might acquire unexpected values

A functional approach to our goal eliminates these side-effect errors altogether.


```python
bigmuls = lambda xs,ys: filter(lambda x,y:x*y > 25, combine(xs,ys))
combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
print(bigmuls((1,2,3,4),(10,15,3,22)))
```

    <filter object at 0x11296b860>


Discussion: The real advantage of this functional example is that absolutely no variables change any values within it. There are no possible unanticipated side-effects on later code (or from earlier code). Obviously, the lack of side-effects, in itself, does not guarantee that the code is correct, but it is nonetheless an advantage.




```python

```
