from itertools import count
from unicodedata import name


class Employee:
    count = 0
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count+=1
    def displayCount(self):
            print("There are %d employees" % Employee.count)
    def displayDetails(self):
            print("Name:", self.name, ", Position:", self.position, ", Salary:", self.salary)

#
emp = Employee("Ilyas Rufai", "DevOps Engineer", 10000000)
emp1 = Employee("Ayo", "HR", 300000)
emp2 = Employee("Aisruffy", "manager", 900000)
emp3 = Employee("Alex", "programmer", 500000)
emp4 = Employee("AbdulRahmon", "Engineer", 45000)

#Count of employees
emp4.displayCount()

#
print("**Information about the Employee**")
emp.displayDetails()
emp1.displayDetails()
emp2.displayDetails()
emp3.displayDetails()
emp4.displayDetails()