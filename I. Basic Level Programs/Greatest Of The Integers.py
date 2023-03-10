Num = int(input("Enter the number of integers you want to enter: \n"))
integerList = []
for i in range(0,Num):
    print("Enter the",i,"st/nd integer:")
    temp = input("integer: \n")
    integerList.append(temp)

integerList.sort(reverse=True)
print("The entered integers in desending order:\n",integerList)
print("The Greatest given integer is:\n",integerList[0])
print("The Second Greatest given integer is:\n",integerList[1])
print("The Third Greatest given integer is:\n",integerList[2])