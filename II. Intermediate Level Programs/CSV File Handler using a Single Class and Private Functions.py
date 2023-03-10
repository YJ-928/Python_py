# There are two types class privates and module privates.
# A Module private starts with ONE underscore
# A Class private starts with TWO underscore

# import libraries
import csv
import os
import time


# Random Data for writing and appending into csv
DataWrite = [["name", "Alice", "age", 25], ["name", "Bob", "age", 30],
             ["name", "Charlie", "age", 35], ["name", "David", "age", 40]
             ]

DataAppend = [
    ["Python", "Machine Learning", "R", "Machine learning"],
    ["Python", "Web development", "Java Script", "Web Development",
     "HTML", "Web Development"],
    ["C++", "Game Development", "Python", "Game Development"],
    ["Java", "App Development", "Kotlin", "App Development"]
]

# Creating a Class CSV_Handler having four key functions


class CSV_Handler():

    # CSV write public function
    def CSVWrite(Path):
        with open(Path, 'w') as __file:
            write = csv.writer(__file)
            write.writerows(DataWrite)
            print("CSV-File Writing Completed")

    # CSV append private function
    def __CSVAppend(Path):
        with open(Path, 'a') as __file:
            write = csv.writer(__file)
            write.writerows(DataAppend)
            print("CSV-File Data Appending Completed")

    # CSV read public function
    def CSVRead(Path):
        with open(Path, 'r') as __file:
            read = csv.reader(__file)
            for row in read:
                print(row)
            print("CSV-File Reading Completed")

    # CSV delete private function
    def __CSVDelete(Path):
        os.remove(Path)
        print("CSV-File All Task Completed, Now Deleting the file:\n")


# Main Code
Path = str(input("Enter CSV file Path/ CSV File Name:\n"))
time.sleep(5)
CSV_Handler.CSVWrite(Path)
time.sleep(5)
# To call Private Classes:
CSV_Handler._CSV_Handler__CSVAppend(Path)
time.sleep(5)
CSV_Handler.CSVRead(Path)
time.sleep(5)
# To call Private Classes:
CSV_Handler._CSV_Handler__CSVDelete(Path)
time.sleep(5)
