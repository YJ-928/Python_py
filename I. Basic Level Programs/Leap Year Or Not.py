def IsLeap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("Is a Leap Year.")
            else:
                print("Not a Leap Year.")
        else:
            print("Is a Leap Year.")
    else:
        print("Not a Leap Year.")

print("Welcome to King-YJ's Leap Year Calculator:\n")
year = int(input("Enter the year:\t"))
IsLeap(year)