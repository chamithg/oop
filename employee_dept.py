#### this is department class

class Department:
    def __init__(self,name):
        self.name = name
        self.employees = []

    def add_employee(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def print_employee_info(self):
        if not self.employees:
            print(f"No employees in {self.name}")
        for employee in self.employees:
            print(f"{employee.first_name[0]}.{employee.last_name} - Salary: {employee.salary}")


    def __str__ (self):
        if len(self.employees)==1:
            return f"{self.name}({len(self.employees)} employee)"

        
#### this is employee class

class Employee():                           # this is the class, functions inside of a class is called methods.
                                            # in python, every class needs an __init__ method(the initialization method.)

    def __init__(self, f_name, l_name, sal, department):  # in the init method always the first arguement is self.
        self.first_name = f_name                          # those are properties
        self.last_name= l_name
        self.salary = sal
        self.department = department
        self.department.add_employee(self)
        
    def full_name(self):                                  # here we define a new method to get the full name by calling it 
        return f"{self.first_name}{self.last_name}"
    
    def set_salary(self, new_salary):                    # this is a specified method to change the salry
        if new_salary > 40000  and new_salary< 250000:   # it has more controll over the changes. (floor and ceiling)
            self.salary = new_salary                     # as a bonus, it checks if the new value is an integer. 
        
department_a = Department("sales")
department_b = Department("engineering")
department_c = Department("HR")
department_d = Department("sales")
department_e = Department("sales")
department_f = Department("sales")



new_employee = Employee("Chamith", "Gamage", 50000, department_a)
new_employee2 = Employee("Aron", "Johnson", 50000,department_b)
new_employee3 = Employee("James", "Bond", 50000, department_c)

employee_list = [new_employee, new_employee2, new_employee3] 


#or.. we can just creat a list of employee objects.

for employee in employee_list:
    print(f'{employee.full_name()}')  # calling the full name method instead of  return f"{employee.first_name}{employee.last_name}"


