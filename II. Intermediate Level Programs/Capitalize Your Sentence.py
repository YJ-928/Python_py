print("Welcome to Capitalize Your Sentences !!!")
myStr = input("Enter the sentence:\n")

# Orignal string containing List
myList = []
# Capitalized Letter string containing List 
capList = []

# This converts our string to a list, .split() functons splits the string at whitespaces.
myList = myStr.split()

# Transfers and Capitalizes each starting letter of the string and stores in another list.
for i in range(0,len(myList)):
    temp = myList[i]
    Temp = temp.capitalize()
    capList.append(Temp)

# Initialize an empty string
capStr = ""

# For Loop to convert our List to a String
for word in capList:
    capStr += word

# Your Each Letter Capitalized String o/p
print(capStr)