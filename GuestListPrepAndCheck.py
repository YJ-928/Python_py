print("Hello, Welcome to King-YJ's Guest List Prepare program.")
HostName = input("Enter your name:\n")
GuestNum = int(input("Enter the number of guests:\n"))
GuestList = []

if GuestNum == 0:
    print("Have you cancelled your party?, no problem, we will be here in case you host another party, Thank you cya soon!")
    exit()

else:
    for n in range(0,GuestNum):
        print("Enter your guest name's for party invitations:")
        temp = input("Name: ")
        GuestList.append(temp)

print("Your guest list is ready, have a look:\n")
print(GuestList)

for n in range(0, GuestNum):
    print("\n Welcome to "+HostName+"'s Party.")
    GuestName = input("Enter your name to check if you are on the guest list:\n")
    if GuestName in GuestList:
        print("Welcome "+GuestName+" have fun.")
        
    else:
        print("Sorry your name is not on the GuestList, better luck next time.")
        n = n - 1
print("That concludes all Guest's, Thank you for using our services.")