import csv

TempList = []
Marks = []
Stu1 = 0
Stu2 = 0
Stu3 = 0
Stu4 = 0
Stu5 = 0
AvgMarks = []

with open("Python Tasks\StudentsData.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        TempList.append(row)
file.close()

for i in range(1, len(TempList)):
    Rows = TempList[i]
    for j in range(1, len(Rows)):
        Marks.append(Rows[j])

for x in range(0, len(Marks)):
    if x in range(0, 5):
        Stu1 = Stu1 + int(Marks[x])
        Stu1 = Stu1/5
    elif x in range(5, 10):
        Stu2 = Stu2 + int(Marks[x])
        Stu2 = Stu2/5
    elif x in range(10, 15):
        Stu3 = Stu3 + int(Marks[x])
        Stu3 = Stu3/5
    if x in range(15, 20):
        Stu4 = Stu4 + int(Marks[x])
        Stu4 = Stu4/5
    if x in range(20, 25):
        Stu5 = Stu5 + int(Marks[x])
        Stu5 = Stu5/5

with open("Python Tasks\StudentsAvgMarks.csv", 'w') as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Average-Marks"])
    writer.writerow(["A", Stu1])
    writer.writerow(["B", Stu2])
    writer.writerow(["C", Stu3])
    writer.writerow(["D", Stu4])
    writer.writerow(["E", Stu5])

file.close()

with open("Python Tasks\StudentsAvgMarks.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        AvgMarks.append(row)
file.close()

print(TempList)
print(AvgMarks)
