# Python dictionary key checker

# Create a Test Dict
MyDict = {"name": "abcd", "age": "23", "gender": "male",
          "number": "1234567890", "email": "abc@example.com"}

# Countinous Loop
while True:
    # Taking input from user
    userInput = input("Enter the key [type 'bye' to exit]:\n")

    # Exit Keyword for breaking the Loop
    if userInput == "bye":
        break

    # Checking if user given key is present in dict
    elif userInput in MyDict:
        print("Key found")
        print(MyDict[userInput])

    # If Key not found
    else:
        print("Key not found!")
