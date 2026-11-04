 Employee Salary Calculator (Python)
## Project Information
Project Name: Employee Salary Calculator
Language: Python 3
Project Type: Console-based application
Main File: employee_salary_calculator.py
Concepts Used: Variables, input/output, functions, loops, conditional statements,
calculations, and input validation.
## Project Overview
This is a simple Python program for calculating an employee's salary. The user enters the
employee's name, employee ID, and basic salary. The program calculates HRA, DA, gross salary,
PF, tax, and net salary, then prints a formatted employee salary slip.
## Features
• Takes employee name and employee ID as input.
• Accepts the employee's basic salary.
• Calculates HRA (20%) and D#A (10%) of basic salary.
• Calculates gross salary by adding basic salary, HRA, and DA.
• Calculates PF (12%) of basic salary.
• Calculates tax according to the gross salary slabs.
• Displays a formatted salary slip with all details.
• Validates empty details and invalid or non-positive salary.
• Allows the user to calculate salary for more than one employee.
## Project Structure
Employee-Salary-Calculator/
|
|-- employee_salary_calculator.py
|-- README.md
|-- README_Employee_Salary_Calculator.pdf
## How to Run
1. Install Python 3 on your computer.
2. Open the project folder in Visual Studio Code (VS Code).
3. Open employee_salary_calculator.py.
4. Click the Run button or run the file from the terminal.
5. Enter the employee name, employee ID, and basic salary when asked.
6. The salary slip will be displayed in the terminal.
## Salary Calculation Rules
Item
Formula / Rule
HRA
20% of Basic Salary
DA
10% of Basic Salary
Gross Salary
Basic Salary + HRA + DA
PF
12% of Basic Salary
Item
Formula / Rule
Tax
0% if gross salary is up to ■25,000
Tax
5% if gross salary is above ■25,000 and up to ■50,000
Tax
10% if gross salary is above ■50,000
Net Salary
Gross Salary − PF − Tax
## How It Works
Function
Purpose
calculate_gross()
Calculates HRA, DA, and gross salary.
calculate_pf()
Calculates the PF deduction.
calculate_tax()
Calculates tax using the given salary slabs.
print_slip()
Calculates and displays the employee salary slip.
main()
Takes input, validates details, and repeats the process if requested.
## Sample Output
Example input: Employee Name = Arshad, Employee ID = 101, Basic Salary = ■30,000.
==========================================
 EMPLOYEE SALARY SLIP
==========================================
Employee Name : Arshad
Employee ID : 101
------------------------------------------
Basic Salary : ■30000.00
HRA (20%) : ■6000.00
DA (10%) : ■3000.00
Gross Salary : ■39000.00
PF (12%) : ■3600.00
Tax : ■1950.00
------------------------------------------
Net Salary : ■33450.00
==========================================
## Test Cases
Scenario
Expected Result
Valid employee details and salary
Salary slip is generated.
Empty employee name or ID
Invalid input message is displayed.
Text entered as salary
Invalid salary message is displayed.
Zero or negative salary
Invalid salary message is displayed.
Gross salary up to ■25,000
Tax is 0%.
Gross salary above ■25,000 and up to ■50,000 Tax is 5%.
Gross salary above ■50,000
Tax is 10%.
## Note
The percentages and tax slabs in this README are based on the supplied project code. They are
project rules for learning purposes and are not official payroll or tax advice.