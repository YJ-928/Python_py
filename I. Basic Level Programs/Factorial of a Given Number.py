# To calculate factorial of the given number.

def factorial(number):
    factoList = []
    facto = 1

    for i in range(1, number):
        factoList.append(i)
        facto = facto * i
    factoList.sort(reverse=True)

    return print(factoList, "\n", "And the value of ", number, "!", "is:", facto)


number = int(input("Enter a number:\n"))
print(number, "! is:")
factorial(number)
