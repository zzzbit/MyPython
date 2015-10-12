'''
Created on 2015年3月17日

@author: zhangzhizhi
'''
class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def display(self):
        print(Employee.empCount)
    
    def displayEmployee(self):
        print(self.name)
        

emp1 = Employee('aaa',12)
emp1.display()
emp1.displayEmployee()