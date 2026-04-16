class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

        self._hra = 0
        self._da = 0
        self._tax = 0
        self._gross_salary = 0
        self._net_salary = 0

    def calculate_salary(self):
        self._hra = 0.20 * self.basic_salary
        self._da = 0.10 * self.basic_salary
        self._tax = 0.05 * self.basic_salary

        self._gross_salary = self.basic_salary + self._hra + self._da
        self._net_salary = self._gross_salary - self._tax

    def display(self):
        print("\n===== Employee Salary Slip =====")
        print(f"Employee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Basic Salary  : {self.basic_salary:.2f}")
        print(f"HRA (20%)     : {self._hra:.2f}")
        print(f"DA (10%)      : {self._da:.2f}")
        print(f"Tax (5%)      : {self._tax:.2f}")
        print(f"Gross Salary  : {self._gross_salary:.2f}")
        print(f"Net Salary    : {self._net_salary:.2f}")


n = int(input("Enter number of employees: "))
employees = []

for _ in range(n):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    emp = Employee(emp_id, name, basic_salary)
    emp.calculate_salary()
    employees.append(emp)

for emp in employees:
    emp.display()
