print("Welcome to King-YJ's Pallindrome Check Program:")
number = input("Enter the number: \t")

RevNum = str(number)[::-1]

if number == RevNum:
    print(number," is a pallindrome.")

else:
    print(number," is not a pallindrome.")