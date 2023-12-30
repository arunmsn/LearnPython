# R-1.01
# Write a short Python function, is_multiple(n,m), that takes two integer values and returns True if n is a multiple of m. Otherwise, return False.
def is_multiple(n,m):
    if n % m == 0:
        return True
    return False
print(is_multiple(6,5))

# R-1.02
# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise.
# No using multiplication, division, or modulus!
"""THERE ARE TWO WAYS!"""
def is_even_1(k):
    if k & 1 == 0:      # using bitwise and (&)
        return True
    return False
print(is_even_1(3))

def is_even_2(k):
    b,c = True, True
    i = 0
    while i < k:    
        b != b          # swiches boolean value every time
        i += 1
    if b == c:
        return True     # if k is even, the boolean value will return to its original value
    return False        # if k is odd, the boolean value will change
print(is_even_2(3))

# R-1.03
# Write a short Python function, minmax(data), that takes a sequence of one or more numbers and returns the min and max values in the form of a two-number tuple.
# No using the built in min and max functions!
def minmax(data):
    maxVal = 0
    for i in data:
        if i > maxVal:
            maxVal = i
    minVal = maxVal
    for j in data:
        if minVal > j:
            minVal = j
    return minVal, maxVal
print(minmax([0,0,0,0,1,2,3,4,0,10,12222,23,24,34,24,5,32,1,34,2647,32,32454,234234,34532,7]))

# R-1.04
# Write a short Python function that takes a positive integer (n) and returns the sum of all the squares of all the positive integers smaller than n.
def sumOfSquares(n):
    sumSquare = 0       # NOTE: using sumSquare b/c sum is a pre-defined function
    i = 1
    while i < n:
        sumSquare += pow(i,2)
        i += 1
    return sumSquare
print(sumOfSquares(5))

# R-1.05
# Give a single command that computes the sum from R-1.04, relying the Python's comprehension syntax and built-in sum function
def sumOfSquares(n):
    sumSquare = sum(i*i for i in range (1, n))
    return sumSquare
print(sumOfSquares(5))

# R-1.06
# Write a short Python function that takes a positive integer (n) and returns the sum of all the squares of all the odd positive integers smaller than n.
def sumOddSquares(n):
    sumOddSquare = 0
    i = 1
    while i < n:
        sumOddSquare += pow(i,2)
        i += 2
    return sumOddSquare
print(sumOddSquares(5))

# R-1.07
# You know the drill -- turn R-1.06 into a single command using comprehension syntax and built-in sum
def sumOddSquares(n):
    sumOddSquare = sum(i*i for i in range (1, n, 2))
    return sumOddSquare
print(sumOddSquares(5))

# R-1.08
# Python allows negative numbers to be used as indices into a sequence, such as a string. 
# If string s has length n, and the expression s[k] is used for index -n <= k < 0 (all indices strictly negative!),
# what is the equivalent index j >= 0 (all indices greater than -1) such that s[j] references the same element?
"""
j is at k when j = 0 and k is -n
          when j = 1 and k is -n+1
          when j = 2 and k is -n+2
          when j = 3 and k is -n+3
          ...
          you see the pattern?
j is at k when k = -n + j
The following program proves so! Plug in different values for j and try it out for yourself!
"""
def jk():
    data = [1,2,3,4,5]
    j = 1
    n = data.__len__()
    k = -n + j
    print(data[j], data[k])
jk()

# R-1.09
# What parameters should be sent to the range constructor to produce a range with values 50,60,70,80?
data = range(50, 81, 10)
for i in data:
    print(i, end=' ')
print()

# R-1.10
# What parameters should be send to the range constructor to produce a range with values 8,6,4,2,0,-2,-4,-6,-8?
data = range(8, -9, -2)
for i in data:
    print(i, end=' ')
print()

# R-1.11
# Demonstrate how to use Python's list comprehension syntax to produce the list [1,2,4,8,16,32,64,128,256].
def powers2List(n):
    return [pow(2,i) for i in range(0,n)]
print(powers2List(9))

# R-1.12
# Python's random module includes a function choice(data) that returns a random element from a non-empty sequence.
# The random module includes a more basic function randrange, with parametrization similar to the built-in range function,
#   that returns a random choice from the given range.
# Using only the randrange function, implement your own version of the choice function.
"""
choice uses a sequence (list, etc.) while randrange uses 3 parameters: start, stop, step
The easiest way to create a list without creating a list is through the range, which we can just use in randrange like the following:
"""
from random import randrange    # randrange isn't built in!
def choiceRandRange():
    return randrange(1, 10000, 1)
# to showcase 5 different numbers:
i = 0
while i < 5:
    if i < 4:
        print(choiceRandRange(), end=", ")
    else:
        print(choiceRandRange())
    i += 1