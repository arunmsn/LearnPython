"""CONDITIONAL EXPRESSIONS"""
# General syntax is the form
# expr1 if condition else expr2

# If you are familiar with Java or C++, you would have seen the following:
# condition ? expr1 : expr2
# Python simply uses a different format

# To get the square root of the absolute value, for example, the following program is written:
def foo(k):
    k ** 0.5
def square_root(n):
    if n >= 0:
        param = n
    else:
        param = -n
    result = foo(param)
    print(result)
    
# but this can be simplifed using conditional expressions:
def foo(k):
    k ** 0.5
def square_root(n):
    param = n if n >= 0 else -n
    result = foo(param)
    print(result)
    
# and its actually not even necessary for defining param:
def foo(k):
    k ** 0.5
def square_root(n):
    print(result = foo(n if n >= 0 else -n))

# to simplify without two functions:
def square_root(n):
    print((n if n >= 0 else -n) ** 0.5)

# NOTE: Of course, in a regular instance abs(x) would be used but this was merely to show example

"""COMPREHENSION SYNTAX"""
# The general form of a comprehension syntax (in this case list comprehension) is:
# [expression for value in iterable if condition]
# This is equivalent to:
# resultList = []
# for value in iterable:
#     if condition:
#         resultList.append(expression)
# An example is for a list of all the perfect squares from 1 to n [so 1, 4, 9, 16, 25, ..., n^2]:
def listOfSquares(n):
    squares = []
    for k in range (1, n+1):
        squares.append(k*k)
# with list comprehension, the code simply becomes:
def listOfSquares(n):
    squares = [k*k for k in range(1, n+1)]
    return squares

# As a nod to 1.8 where we got the factors for a specified number, the following can be written:
def listOfFactors(n):
    factors = [k for k in range(1, n+1) if n % k == 0]
    return factors

# And comprehension syntax is not limited to list, it can be used for set, generator, and dictionary as well:
def comprehension(n):
    squaresList = [k*k for k in range(1, n+1)]
    squaresSet = {k*k for k in range(1, n+1)}
    squaresGenerator = (k*k for k in range (1,n+1))
    squaresDictionary = {k : k*k for k in range(1, n+1)}
    return squaresList, squaresSet, squaresGenerator, squaresDictionary

"""PACKING AND UNPACKING OF SEQUENCES"""
# When instantiating
data = 2,4,6,8
# it actually instantiates to be the tuple (2,4,6,8), and this behavior is known as AUTOMATIC PACKING
# A common use of automatic packing is when returning values:
def toReturn(x,y):
    return x,y
# which actually returns the tuple (x,y)

# And Python does the AUTOMATIC UNPACKING as well, the opposite of packing:
a,b,c,d = range(7,11)       # a=7, b=8, c=9, d=10
# This can be used to unpack the return tuples from programs, as such:
def QuoAndRem():
    quotient, remainder = divmod(a,b)
    # through this, quotient=a/b and remainder = a%b
    return ("The quotient is ", quotient, " and the remainder is ", remainder)
# Also, this is useful for iterating over a sequence of iterables, like the following:
for x,y in [(1,2), (3,4), (5,6), (7,8)]:
    print(x+y)
# And suppose there is a map with items, we can use the two variables to represnt key and value:
mapping = {1:2, 3:4, 5:6, 7:8}
for k,v in mapping.items():
    print(k+v)

# As you would have realized already, we can use this for simultaneous assignments of variables (as seen with the range example).
# A better visual example is the following:
x,y,z = 1,2,3
# And those annoying times where we swap variable values:
k,j = 2,3
temp = j
k = j
k = temp
# become as simple as:
k,j = 2,3
j,k = k,j       # this is the condesation of the three lines, also without using the temp variable

# Remember fibonacci from 1.8? Here's the simpler version:
def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b     # so a=b and b=a+b