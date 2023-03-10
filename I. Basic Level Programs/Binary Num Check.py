num = int(input("please give a number : "))
while (num > 0):
    j = num % 10
    if j != 0 and j != 1:
        print("number is not binary")
        break
    num = num//10
    if num == 0:
        print("number is binary")