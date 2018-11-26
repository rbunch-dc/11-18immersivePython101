class Employee(object):
  def __init__(self, name, salary):
     self.name = name
     self.salary = salary
    #  Employee.empCount += 1

  def displayCount(self):
    print "Total Employee %d" % 1

  def displayEmployee(self):
     print "Name : ", self.name,  ", Salary: ", self.salary

# def displayEmployee(name, salary):


emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
# 'Common base class for all employees'
# empCount = 0

# print emp1.name
# print emp2.name
# print emp2.salary
# displayEmployee("Sean",100000)
emp1.displayEmployee()
emp2.displayEmployee()