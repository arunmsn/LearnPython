"""CREATIVITY"""
# C-1.13
# Write a pseudocode description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order
#   than they were before, and compare this method to an equivalent Python function for doing the same thing.
"""
Use sequence data as a parameter to the function.
Inside the function:
    Create a new, empty sequence
    Using negative indices, place into the new sequence each integer
        The new sequence will now be the old in reverse order
    Set the old sequence to be the new sequence

In Python, there is a function called reversed(), which takes no parameter, and reverses the sequence.
"""

# C-1.14
# Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence
#   whose product is odd
"""THERE ARE TWO WAYS"""
#1
def oddProd(data):
    seq = []
    seq.extend(data)
    seq.clear()
    for i in data:
        if i % 2 == 1:
            seq.append(i)
    if seq.__len__() > 1:
        return True
    return False
data = {1,2,3,4}
print(oddProd(data))

#2
def oddProd(data):
    for i in range(len(data)):
        if list(data)[i] % 2 == 1:              # we have to type-cast data from any type into a list
            for j in range(i+1, len(data)):     
                if list(data)[j] % 2 == 1:      # same here, type-casting data
                    return True
    return False
data = {1,2,3,4}
print(oddProd(data))

# C-1.15
# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.
def uniqueList(data):
    if len(set(data)) == len(data):                     # remember how a set contains only unique numbers? Review 1.02!
        print("The set has all distinct elements.")
    else:
        print("The set has repeated numbers.")
data = {1,2,3,4,5,6,7,8,9,10,11,12,2}
uniqueList(data)

# C-1.16
# In our implementation of the scale function, the body of the loop executes the command data[j] *= factor.
# We have discussed that numeric types are immutable, and the use of the *= operator in this context causes the creation of
#   a new instance (not the mutation of an existing instance). 
# How is it still possible, then, that our implementation of scale changes the actual parameter sent by the caller?
"""
When we programmed it, we have data[j] *= factor.
What this actually does is data[j] = data[j] * factor, so we just set data[j] to be the new value.
The new value is set at the same index as the old one, so the actual parameter ends up changing!
"""

# C-1.17
# Had we implemented the scale function as follows, does it work properly?
def scale(data, factor):
    for val in data:
        val *= factor
"""Well, the only way to know for sure is to try it out!"""
seq=[1,2,3,4]
scale(seq, 2)
print(seq)
"""
The answer you should get is [1,2,3,4], which is not scaled. This is due to actual value in data not changing, just the val we are retrieving!
The actual values in seq aren't actually chaning.
"""

# C-1.18
# Demonstrate how to use Python's list comprehension syntax to produce the list [0,2,6,12,20,30,42,56,72,90]
"""
The pattern to notice here is that it follows +2, +4, +6, +8, ...
But that doesn't really help us here.
The real pattern to notice here is the factors of each:
0  - 0
2  - 1,2
6  - 1,6 2,3
12 - 1,12 2,6 3,4
...
Notice how the last of each list are numbers right next to each other?
The smart play here is to relate it to the index position
When looking at the numbers, the pattern follows:
    index * (index+1)
Let's program it!
"""
def indexBasedList(n):
    print([i*(i+1) for i in range(0,n)])
indexBasedList(10)

# C-1.19
# Demonstrate how to use Python's list comprehension syntax to produce the list ['a', 'b', 'c', 'd', ..., 'z']
#   but without having type all 26 letters literally.
"""
Simplest way is to use unicode characters, using the chr function
"""
def charList():
    print([chr(i) for i in range(ord('a'),ord('z')+1)])     # notice the range is based on ord(), so it's the unicode range!
charList()                                                  # the unicode is converted to characters through chr().

# C-1.20
# Python's random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each
#   possible order occurs with equal probability. 
# The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including the endpoints a and b). 
# Using only the randint function, implement your own version of shuffle.
from random import randint
def randIntShuffle(data):
    dataList = list(data)
    for i in range(len(dataList)):
        shuffleInt = randint(0,len(dataList)-1)
        dataList[i], dataList[shuffleInt] = dataList[shuffleInt], dataList[i]
    data = dataList    
    return data   
setNum = {14, 12, 9, 8, 5, 6, 0, 1, 7, 13, 13}
print(randIntShuffle(setNum))

# C-1.21
# Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs those lines in reverse order.
# (a user can indicate end of input by typing ctrl+D) [on my system, the input is ctrl+Z; try that if ctrl+D isn't working]

def reverseInput():
    print("Input Here!")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        for line in reversed(lines):
            print(line)
# reverseInput()

# C-1.22
# Write a short Python program that takes two arrays, a and b, of length n storing int values, and returns the dot product of a and b.
"""THERE ARE TWO WAYS"""
def arrayDotProd(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c
a = [1,2,3]
b = [2,3,4]
print(arrayDotProd(a,b))

def arrayDotProdComp(a,b):
    c = [a[i]*b[i] for i in range(len(a))]  # Comprehension syntax saving us 2 lines of work!
    return c
print(arrayDotProdComp(a,b))

# C-1.23
# Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds.
# If that index is out of bounds, the program should catch the exception that results, and print the following error message:
#   "Don't try buffer overflow attacks in Python!"
toChange = [1, 2, 3, 4, 5]
def bufferOverflow():
    for i in range(toChange.__len__()+1):
        try:
            toChange[i] *= 2
        except IndexError:
            print("Don't try buffer overflow attacks in Python!")
bufferOverflow()

# C-1.24
# Write a short Python function that counts the number of vowels in a given character string.
def numVowels(given):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in given:
        if letter in vowels:
            count += 1
    return count
print(numVowels("AEIOU"))

# C-1.25
# Write a short Python function that takes a string s, representing a sentence, and returns a copy of the string will all punctuation removed.
# For example, if given the string "Let's try, Mike", the function would return "Lets try Mike" [the apostrophe and comma removed].
def removePunc(given):
    punc = '~`!@#$%^&*()_-+={[}]|\}:;\"\'<,>.?/'
    for letter in given:
        if letter in punc:
            given = given.replace(letter, '')
    print(given)
removePunc("He!llo!")

# C-1.26
# Write a short program that takes as input three integers [a,b,c] from the console the determines if they can be used in a correct arithmetic formula (in the given order):
#   like a+b = c, a-b = c, a*b = c, a/b = c, a%b = c
def arithForm(a,b,c):
    a, b, c = float(a), float(b), float(c)
    if (a+b == c):
        print("Yes, addition!")
        return True
    elif (a-b == c):
        print("Yes, subtraction!")
        return True
    elif (a*b == c):
        print("Yes, multiplication!")
        return True
    elif (a/b == c):
        print("Yes, division!")
        return True
    elif (a%b == c):
        print("Yes, modulus!")
        return True
    else:
        print("These cannot be used in an arithmetic formula!")
        return False
arithForm(2,2,3)

"""If you don't care about which formula works:"""
def arithFormBool(a,b,c):
    a, b, c = float(a), float(b), float(c)
    if (((a+b == c) | (a-b == c) | (a*b == c) | (a/b == c) | (a%b == c))):
        return True
    return False
print(arithFormBool(1,2,3))

# C-1.27
# In Section 1.08, I provided three different implementations of a generator that computes factors for a given integer.
# The third of those implementations was the most efficient, but we noted that it did not yield the factors in increasing order.
# Modify the generator so that it reports the factors in increasing order while maintaining its performance advantages.
"""
As a reminder, this is the implementation the question is referring to:
def factors (i):
    k = 1
    while pow(k,2) < i:     # while k < sqrt(n)
        if i % k == 0:
            yield k
            yield i // k
        k += 1
    if pow(k,2) == i:       # special case: n is a perfect square
        yield               # ensures the root is not repeated (so in 100, 10 only appears once)
"""
def factors(i):
    factors = []
    k = 1
    while pow(k,2) < i:     # while k < sqrt(n)
        if i % k == 0:
            factors.append(k)
            factors.append(i//k)
        k += 1
    if pow(k,2) == i:       # special case: n is a perfect square
        factors.append(k)   # ensures the root is not repeated (so in 100, 10 only appears once)
    factors.sort()
    for factor in factors:
        yield factor
    return factors
print(factors(100))

# C-1.28
# The p-norm of a vector v = (v1, v2, ..., vn) in n-dimensional space is defined as:
# ||v|| = prt(v1^p + v2^p + ... + vn^p)     # this is the pth root (similar to sqrt but prt)
# For the special case p = 2, this is the Euclidean norm, which represents the length of a vector (sqrt, essentially, using pythagorean for vectors)
#   An example is the vector from (0,0) to (4,3) = <4,3>, which has a length of sqrt(4^2 + 3^2) = sqrt(25) = 5
# Give an implementation of a function named norm such that norm(v,p) returns the p-norm value of v and norm(v) returns the Euclidean form (so p = 2)
# You may assume that v is a list of numbers
def norm(v, p=2):
    sum = 0
    for element in v:
        element = pow(element, p)   # 1st step, raise each element to power of p
        sum += element              # 2nd step, add to net sum inside the root   [loop 1 & 2 until all elements in v are covered]
    return (sum ** (1/p))           # 3rd step, raise entire sum to power 1/p (which is prt)
print(norm([4,3]))
print(norm([1,2,3], 3))