"""PROJECTS"""
# P-1.29
# Write a Python program that outputs all possible strings formed by using the characters
#   'c', 'a', 't', 'd', 'o', 'g'
# exactly once.
def possibilities(entryList):
    if len(entryList) == 0:
        return []
    elif len(entryList) == 1:
        return [entryList[0]]
    else:
        result = []
        for i in range(len(entryList)):
            first = entryList[i]
            then = entryList[:i] + entryList[i+1:]
            for perm in possibilities(then):
                result.append(first+perm)

    return result

print(possibilities(['c', 'a', 't', 'd', 'o', 'g']))   

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
def giveChange():
    charged = float(input("Enter the charged amount: "))
    given = float(input("Enter the given amount: "))
    net = given - charged
    
    currency = {
                'name' : 'USD',
                'symbol' : '$',
                'denominations' : {
                                    '100 bill': 100,
                                    '50 bill' : 50,
                                    '20 bill' : 20,
                                    '10 bill' : 10,
                                    '5 bill' : 5,
                                    '1 bill' : 1,
                                    'dollar coin' : 1,
                                    'quarter' : 0.25,
                                    'dime' : 0.1,
                                    'nickel' : 0.05,
                                    'penny' : 0.01
                                  }
               }

    denominations = currency['denominations']
    count = 0
    result = {}
    for denomination, value in denominations.items():
        if net >= value:
            count = int(net // value)
            result[denomination] = count
            net -= (count * value)
    return result 
print(giveChange())

# P-1.31
# Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output device.
# That is, each input to the calculator, be it a number (like 12.34 or 1234) or an operator (like +, -, *, /, %), can be done on a separate line.
# After each such input, you should output to the Python console what would be displayed on your calculator.
def simpleCalculator():
    print("Input Here! Type 'end' to finish input.")
    program = []
    while True:
        if input != '':
            line = input()
        if line == "end":
            break
        program.append(line)

    for line in program:
        print(line, end=" ")
    print()
    final = 0
    for i in range(len(program)):
        if program[i] == '+':
            final += (float(program[i-1]) + float(program[i+1]))
            program[i+1] = final
        elif program[i] == '-':
            final += (float(program[i-1]) - float(program[i+1]))
            program[i+1] = final
        elif program[i] == '*':
            final += (float(program[i-1]) * float(program[i+1]))
            program[i+1] = final
        elif program[i] == '/':
            final += (float(program[i-1]) / float(program[i+1]))
            program[i+1] = final
        elif program[i] == '%':
            final += (float(program[i-1]) % float(program[i+1]))
            program[i+1] = final
        else:
            pass

    print("Final result:", final)
simpleCalculator()
