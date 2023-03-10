# Multi-Level Inheritance using Classes

# Super / Main Class
# Contains properties of Super Class only
class Father:

    def Names(self):
        print("Yash")

# First Derived Class from Main Class
# Contains properties of Super Class + DerivedClass


class Child(Father):

    def ages(self):
        print("23")

# Second Derived Class from First Derived Class
# Contains properties of Super Class +  First-DerivedClass + Second-DerivedClass


class Children(Child):

    def gender(self):
        print("male")


# Defining an object for Child class
Info = Children()

# Accessing Data from all classes
Info.Names()
Info.ages()
Info.gender()
