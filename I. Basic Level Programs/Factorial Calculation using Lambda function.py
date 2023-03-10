# To calculate factorial using Lambda function

# Take a number as input from user
num = int(input("Enter a Number:\n"))

# reduce is used to decrement the value of variable
# lambda function is used to calculate factorial
# print is used to display the output
print reduce(lambda x, y: x*y, range(1, num+1))
