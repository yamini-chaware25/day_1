employees = []


def add_employee():
    emp_id = input("Enter Employee ID: ")

    # Check duplicate ID
    for emp in employees:
        if emp["id"] == emp_id:
            print("Employee ID already exists!")
            return

    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    print("Employee added successfully!")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")

    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter new Name: ")
            emp["department"] = input("Enter new Department: ")
            emp["salary"] = float(input("Enter new Salary: "))

            print("Employee updated successfully!")
            return

    print("Employee not found!")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully!")
            return

    print("Employee not found!")


def search_employee():
    keyword = input("Enter Employee ID or Name: ").lower()

    found = False

    for emp in employees:
        if keyword in emp["id"].lower() or keyword in emp["name"].lower():
            print_employee(emp)
            found = True

    if not found:
        print("Employee not found!")


def list_employees():
    if not employees:
        print("No employees available.")
        return

    print("\n----- Employee List -----")

    for emp in employees:
        print_employee(emp)


def print_employee(emp):
    print(
        f"ID: {emp['id']} | "
        f"Name: {emp['name']} | "
        f"Department: {emp['department']} | "
        f"Salary: ₹{emp['salary']:.2f}"
    )


def highest_salary():
    if not employees:
        print("No employees available.")
        return

    employee = max(employees, key=lambda emp: emp["salary"])

    print("\n----- Highest Salary -----")
    print_employee(employee)


def average_salary():
    if not employees:
        print("No employees available.")
        return

    total = sum(emp["salary"] for emp in employees)
    average = total / len(employees)

    print(f"\nAverage Salary: ₹{average:.2f}")


def department_filter():
    department = input("Enter Department: ").lower()

    found = False

    print(f"\n----- Employees in {department} -----")

    for emp in employees:
        if emp["department"].lower() == department:
            print_employee(emp)
            found = True

    if not found:
        print("No employees found in this department.")


def main():
    while True:
        print("\n==============================")
        print("   EMPLOYEE MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Highest Salary")
        print("7. Average Salary")
        print("8. Department Filter")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            update_employee()

        elif choice == "3":
            delete_employee()

        elif choice == "4":
            search_employee()

        elif choice == "5":
            list_employees()

        elif choice == "6":
            highest_salary()

        elif choice == "7":
            average_salary()

        elif choice == "8":
            department_filter()

        elif choice == "9":
            print("Thank you for using Employee Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()