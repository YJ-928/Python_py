# To check and extract the people of age 30 & above from the List of Dictionaries
# Given List of dictionaries
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30},
          {"name": "Charlie", "age": 35}, {"name": "David", "age": 40}]

# Extracting ppl of age 30 & above
for items in people:
    data = list(items.values())
if data[1] >= 30:
    print(data[0])
