def LifeLeft(YourAge):
    age = (100 - YourAge)
    days = (age * 365)
    weeks = (age * 52)
    months = (age * 12)
    strDays = str(days)
    strWeeks = str(weeks)
    strMonths = str(months)
    print("Life Left with you is: " + strDays + " Days, "+ strWeeks +" Weeks and "+ strMonths +" Months.")

print("Welcome to King-YJ's Life Left Calculator: \n")
YourAge = int(input("Enter your age: \n"))
LifeLeft(YourAge)