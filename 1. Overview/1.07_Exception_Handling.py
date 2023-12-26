"""
COMMON EXCEPTION TYPES
CLASS               DESCRIPTION
Exception           A base class for most error types
AttributeError      Raised by sintax onj.foo, if obj has no member named foo
EOFError            Raised if "end of file" reached for console or file input
IOError             Raised upon failure of I/O operation (e.g., opening file)
IndexError          Raised if index to sequence is out of bounds
KeyError            Raised if nonexistent key requested for set or dictionary
KeyboardInterrupt   Raised if uses types ctrl-C while program is executing (unsure for macOS)
NameError           Raised if nonexistent identifier used
StopIteration       Raised by next(iterator) if no element
TypeError           Raised when worng type of paramter is sent to a function
ValueError          Raised when parameter has invalid value (e.g., sqrt(-5), int('hello'))
ZeroDivisionError   Raised when any division operator used with 0 as divisor (e.g., 2/0)
"""
raise ValueError('x cannot be negative')        # an example of a ValueError being raised

# an example program with many raised errors
def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    # do the real work here

def sum(values):
    if not isintance(values, colletions.Iterable):
        raise TypeError('parameter must be an iterable type')
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total += v
    return total

# a more direct approach to sum (though making assumptions)
def sumDirect(values):
    total = 0
    for v in values:
        total += v
    return total
# this version behaves exactly like Python's built in summation feature
# when inputting say sum([3.14, 'oops']) the error message is as follows:
# unsupported operand type(s) for +: 'float' and 'str'
# when inputting say sum(["all", "be"]), the error message is weird, since the ouput is a int and string addition error (due to total being 0 initially)

# in most cases, we well use "look before you leap" to avoid any exceptions needing to be raised (unless absolutely necessary)
# For a division, we could use:
if y != 0:
    ratio = x/y;
else:
    # do something else
    print("y is zero! Try again!")

# another possibility is the try-except control structure, as follows:
try:
    ratio = x/y;
except ZeroDivisionError:
    print("y is zero! Try again!")

try:
    fp = open("sample.txt")
except IOError as e:
    print("Unable to open the file:", e)

# as a nod to 1.6's age example, we can do the following:
age = int(input("Enter you age in years: "))
# since this one could fail for several reasons, we should do the following:
age = -1        # an invalid input
while age <= 0:
    try:
        age = int(input("Enter your age in years: "))
        if age <= 0:
            print("Your age must be positive!")
    except (ValueError, EOFError):
        print("Invalid response!")
        pass    # this just skips the issue rather than stopping the program from flowing

# another way to do the same, but being more specific with errors:
age = -1
while age <= 0:
    try:
        age = int(input("Enter your age in years: "))
        if age <= 0:
            print("Your age must be positive!")
    except ValueError:
        print("That is an invalid age specification.")
    except EOFError:
        print("There was an unexpected error reading input.")
        raise       # this re-raises the exception
    finally:        # simply here to show the "finally" of the try-except-finally structure
        pass