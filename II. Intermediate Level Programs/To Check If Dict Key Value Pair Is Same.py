# Python3 code to demonstrate
# check for unique values
# Using loops

# initializing dictionary
test_dict = {'Manjeet': 1, 'Akash': 2, 'Akshat': 3, 'Nikhil': 1}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# using loops
# check for unique values
flag = False
hash_val = dict()
for keys in test_dict:
    if test_dict[keys] in hash_val:
        flag = True
        break
    else:
        hash_val[test_dict[keys]] = 1

# print result
print("Does dictionary contain repetition : " + str(flag))
