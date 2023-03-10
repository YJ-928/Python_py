print(" Welcome to King-YJ Bmi-Calculator! ")
weight = int((input("Enter your weight (in Kg): ")))
height = int((input("Enter your height (in m): ")))
heightSq = (height * height)
bmi = (weight/heightSq)
print("Your BMI is:",bmi)
if (bmi < 18.5):
    print("You are under weight.")
elif (bmi >= 18.5 and bmi <=24.9):
    print("You are normal weight.")
else:
    print("You are over weight.")