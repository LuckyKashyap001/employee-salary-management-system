# 💼 Employee Salary Management System (Python)

## 📌 Overview  

This is a simple **Employee Salary Management System** built using Python and Object-Oriented Programming (OOP) concepts.  
The system helps manage employee details and automatically calculates salary components such as allowances and deductions.

It reduces manual errors, improves efficiency, and provides a structured way to generate salary reports.

---

## 🎯 How the System Works  

1. User enters employee details:
   - Employee ID  
   - Name  
   - Basic Salary  

2. The system calculates:
   - HRA (House Rent Allowance)  
   - DA (Dearness Allowance)  
   - Tax deduction  

3. It computes:
   - Gross Salary  
   - Net Salary  

4. Displays a formatted salary slip for each employee  

5. Supports multiple employees  

---

## 🧩 Features  

* ✅ Object-Oriented Design (Class & Object)  
* ✅ Encapsulation of salary data  
* ✅ Automatic salary calculations  
* ✅ Handles multiple employees  
* ✅ Clear salary slip output  
* ✅ Scalable and easy to extend  

---

## 🖥️ Requirements  

* Python 3.x  

No external libraries required.

---

## ▶️ How to Run  

1. Save the program in a file, for example:  
employee_salary.py

2. Open terminal or command prompt  

3. Run the program:  
python employee_salary.py

---

## 🕹️ Example Output
Enter number of employees: 1
Enter Employee ID: 101
Enter Name: Rahul
Enter Basic Salary: 50000

===== Employee Salary Slip =====
Employee ID : 101
Name : Rahul
Basic Salary : 50000.00
HRA (20%) : 10000.00
DA (10%) : 5000.00
Tax (5%) : 2500.00
Gross Salary : 65000.00
Net Salary : 62500.00

---

## 🛠️ Customization  

### ➤ Change allowance percentages  

```python
self._hra = 0.20 * self.basic_salary
self._da = 0.10 * self.basic_salary
self._tax = 0.05 * self.basic_salary
