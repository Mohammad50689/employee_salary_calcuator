
def calculate_gross(basic_salary):
    """Calculate HRA, DA, and gross salary."""
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross = basic_salary + hra + da
    return hra, da, gross


def calculate_pf(basic_salary):
    """PF is 12% of basic salary."""
    return basic_salary * 0.12


def calculate_tax(gross_salary):
    """Calculate tax using the slabs given in the project statement."""
    if gross_salary <= 25000:
        return 0
    elif gross_salary <= 50000:
        return gross_salary * 0.05
    else:
        return gross_salary * 0.10


def print_slip(name, employee_id, basic_salary):
    """Calculate and print one employee's salary slip."""
    hra, da, gross = calculate_gross(basic_salary)
    pf = calculate_pf(basic_salary)
    tax = calculate_tax(gross)
    net_salary = gross - pf - tax

    print("\n" + "=" * 42)
    print("             EMPLOYEE SALARY SLIP")
    print("=" * 42)
    print(f"Employee Name : {name}")
    print(f"Employee ID   : {employee_id}")
    print("-" * 42)
    print(f"Basic Salary  : ₹{basic_salary:.2f}")
    print(f"HRA (20%)     : ₹{hra:.2f}")
    print(f"DA (10%)      : ₹{da:.2f}")
    print(f"Gross Salary  : ₹{gross:.2f}")
    print(f"PF (12%)      : ₹{pf:.2f}")
    print(f"Tax           : ₹{tax:.2f}")
    print("-" * 42)
    print(f"Net Salary    : ₹{net_salary:.2f}")
    print("=" * 42)


def main():
    print("EMPLOYEE SALARY CALCULATOR")
    print("--------------------------")

    while True:
        name = input("\nEnter employee name: ").strip()
        employee_id = input("Enter employee ID: ").strip()

        if not name or not employee_id:
            print("Invalid input. Name and employee ID cannot be empty.")
            continue

        try:
            basic_salary = float(input("Enter basic salary (₹): "))
        except ValueError:
            print("Invalid salary. Enter a positive number.")
            continue

        if basic_salary <= 0:
            print("Invalid salary. Enter a positive number.")
            continue

        print_slip(name, employee_id, basic_salary)

        again = input("\nCalculate salary for another employee? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thank you for using Employee Salary Calculator.")
            break


if __name__ == "__main__":
    main()