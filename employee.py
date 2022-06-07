class Employee():   # this is the class, functions inside of a class is called methods.
    # in python, every class needs an __init__ method(the initialization method.)

    def __init__(self, f_name, l_name, sal):  # in the init method always the first arguement is self.
        self.first_name = f_name   # those are properties
        self.last_name= l_name
        self.salary = sal
     
    def full_name(self):    # here we define a new method to get the full name by calling it 
        return f"{self.first_name}{self.last_name}"
    
    def set_salary(self, new_salary):       # this is a specified method to change the salry
        if new_salary > 40000  and new_salary< 250000:  # it has more controll over the changes. (floor and ceiling)
            self.salary = new_salary            # as a bonus, it checks if the new value is an integer. 
        
new_employee = Employee("Chamith", "Gamage", 50000)
new_employee2 = Employee("Aron", "Johnson", 50000)
new_employee3 = Employee("James", "Bond", 50000)

employee_list = [new_employee, new_employee2, new_employee3] 


#or.. we can just creat a list of employee objects.

for employee in employee_list:
    print(f'{employee.full_name()}')  # calling the full name method instead of  return f"{employee.first_name}{employee.last_name}"
