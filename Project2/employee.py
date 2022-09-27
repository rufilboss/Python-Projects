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
            print("There are %d employee" % Employee.count)
        def displayDetails(self):
            print("Name:", self.name, "position:", self.position, "salary:", self.salary)