"""PROJECTS"""
# P-1.29
# Write a Python program that outputs all possible strings formed by using the characters
#   'c', 'a', 't', 'd', 'o', 'g'
# exactly once.
from random import *
def possibilities(entryList):
    if len(entryList) == 1:
        return [entryList[0]]
    

# P-1.30
# Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly
#   divide this number by 2 before getting a value less than 2.
def howManyTwos(num):
    count = 0
    while num/2 > 1:
        count += 1
        num /= 2
    return count

from math import log2
def howManyTwosLog(num):
    return round(log2(num))

print(howManyTwos(10))
print(howManyTwosLog(10))

# P-1.31
# Write a Python program than can "make change."
# Your program should take two numbers as input, one that is a monetary amount charged and the other that is a monetary amount given.
# It should then return the number of each kind of bill and coin to give back as change for the difference between the amount given and
#   the amount charged.
# The values assigned to the bills and coins can be based on the monetary system of any current or former government.
# Try to design your program so that it returns as few bills and coins as possible.
def giveChange(charged, given):
    net = given - charged
    