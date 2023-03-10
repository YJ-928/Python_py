import random

print("Welcome to King-YJ's Love Calculator. \n")
YourName = input("Enter your name: \t")
TheirName = input("Enter their name: \t")

RandomList = []

for i in range(0,100):
    RandomList.append(i)

LoveScore = random.choice(RandomList)

if LoveScore >= 70:
    print(YourName+" Loves "+TheirName+" more than anything in this Universe.")
    print(LoveScore)
else:
    print("Love Score is: ")
    print(LoveScore)