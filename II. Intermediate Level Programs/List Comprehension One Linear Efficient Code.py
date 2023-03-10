# To check and extract the people of age 30 & above from the List of Dictionaries
# Given List of dictionaries
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30},
          {"name": "Charlie", "age": 35}, {"name": "David", "age": 40}]

# Syntax == List Comprehension:- [<Variable> <Loop> <Condition> (Optional)]
data = [Info["age"] for Info in people if Info["age"] >= 30]
print(data)
