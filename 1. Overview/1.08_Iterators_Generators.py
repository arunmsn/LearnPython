"""ITERATORS"""
# The for-loop syntax we are used to is the following:
# for element in iterable

# an ITERATOR is an object that manages an iteration through a series of values.
# If variable i identifies an iterator object, then each call to the built in function, next(i)
# next(i) produces a subsequent element from the underlying serie, with a StopIteration exception raised to indicate that there are no further elements.

# an ITERABLE is an object (obj) that produces an iterator via the sybtax iter(obj)

data = [1,2,4,8]        # this is an iterable
i = iter(data)          # this is an iterator
next(i)                 # this returns the next element in data

# So when using a for-loop:
for j in data:
    print(j, end=" ")
print()
# the process of making an iterator to go through the list is automated

# The iterator when calling iter(data) does not store a copy of the list, but rather its current index within the list and represents the next element to be reported
# Thus, if the contents of the original list is updated after the iterator is constructed, the iterator will now report the updated list rather than the original

# Python also supports functions/classes that produce implicit iterable series of values
range(1000000)          # this does not return a list of numbers but rather an iterable range object, known as lazy evaluation
                        # it only produces the numbers, one-by-one as needed, not all 1000000 at once
                        # this is helpful because if the program were to be interruped, not all 1000000 integers were wasting memory, just the one produced at the moment
# the example for using this range is the following:
for j in range(100):                        # only numbers to print are 0-99
    if (j < 99):
        print(j, ", ", sep='', end='')      # prints 0-98, each separated with a comma
    else:
        print(j, sep='', end='')            # prints 99
print()

"""GENERATORS"""
# a GENERATOR is implemented with a syntax that is very similar to a function
# instead of returning values, a yield statement is executed to indicate each element of the series
# for example, to find the factors of a number, the following is implemented:
def factors(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results
# but with generators, the following is implemented:
def factors(num):
    for k in range(1, num+1):
        if num % k == 0:
            yield k             # the fact we are using yield rather than return indicates to Python that this is a generator
# to improve the efficiency of the program, we can use generators to go up only until the square root of the number (say we have 100, the root would be 10)
# the list of factors of 100 are 1,2,4,5,10,20,25,50,100 --> 10 is the root, and is the max number we have to get to using the following program:
def factors (i):
    k = 1
    while pow(k,2) < i:     # while k < sqrt(n)
        if i % k == 0:
            yield k
            yield i // k
        k += 1
    if pow(k,2) == i:       # special case: n is a perfect square
        yield               # ensures the root is not repeated (so in 100, 10 only appears once)

# while for these examples, we can physically set the limit (n, num, i), how about a situation where we can't?
# let's look at the fibonacci sequence
def fibonacci():
    a = 0
    b = 1
    while True:             # goes onto infinity
        yield a             # reports current value of a
        future = a + b
        a = b               # next value to be reported
        b = future          # then this number is reported
# FUN FACT: when print(fibonacci()) is done, the output is not the numbers but rather <generator object fibonacci at 0x...>
# Try it out!