# To check and extract the people of age 30 & above from the List of Dictionaries

# Given List of dictionaries
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30},
          {"name": "Charlie", "age": 35}, {"name": "David", "age": 40}]

# creating an empty list
TempList = []

# first loop to break the list in 4 sub lists
for i in range(0, len(people)):
    TempList.append(people[i])

# second Loop to further divide each sublist to singular dictionaries
for j in TempList:
    Temp = j

    # Keys and values are seperated and stored in singular lists
    keys = list(Temp.keys())
    values = list(Temp.values())
    # If the age is greater than 30, the persons name is printed as output
    if (values[1] >= 30):
        print(values[0])
    else:
        continue
