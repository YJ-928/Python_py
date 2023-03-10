import random

print("Welcome to King-YJ's 'Whose Paying Today !!' program.")
numPpl = int(input("Enter the total number of people present:\n"))

PeopleList = []

print("\nEnter all your names:")

for i in range(0,numPpl):
    temp = input("Name:\t")
    PeopleList.append(temp)

print("\nLet's see who is the lucky person that is buying today:")
print(random.choice(PeopleList))