# try: code that may cause exception
# except: code to run when exception occurs
# finally: code that executes after except is executed

# Example-1: Denominator Cannot be 0 error
try:
    a = 10
    b = int(input("Enter Denominator Value:\n"))
    print(a/b)
except ZeroDivisionError:
    print("Error: Denominator cannot be 0.\n")


# Example-2: Index out of bound error
try:

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(numbers)
    num = int(input("Enter the list index value to be extracted: \t"))
    print(numbers[num])

except IndexError:
    print("Index Out of Bound. \n")


# Example-3: try ,except & else usage
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number! \n")
else:
    reciprocal = 1/num
    print(reciprocal)

# Example-4: IO Error
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

# Example-5: Conditional Exceptions using raise
x = input("Enter any number:\t")

if x < 0:
    raise Exception("Sorry, no numbers below zero")
