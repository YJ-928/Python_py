print("Welcome to the FizzBuzz Challenge.\n")
num = int(input("Enter the nth value to generate FizzBuzz Sequence:\n"))

FizzBuzzSeq = []

for i in range(1,num+1):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
        FizzBuzzSeq.append("FizzBuzz")
        continue
    elif (i % 3 == 0):
        print("Fizz")
        FizzBuzzSeq.append("Fizz")
        continue
    elif (i % 5 == 0):
        print("Buzz")
        FizzBuzzSeq.append("Buzz")
        continue
    else:
        print(i)
        FizzBuzzSeq.append(i)

print("Whole FizzBuzz in a List/Array Form:")
print(FizzBuzzSeq)