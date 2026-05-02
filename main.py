employees = {}
overtimes = {}

def get_employe_name():
    while True:
        employee_name = input(
            "Please enter the name (end with 'done'): "
            ).strip().lower
        
        if any(char.isdigit() for char in employee_name):
            print("Only letters are allowed!")
            continue
        
        elif employee_name == "done":
            return None
        
        else:
            return employee_name
        
def get_hours_worked():
    while True:
        try:
            user_input = input(
                "Please enter the hours worked: "
            ).replace(",", ".").replace(" ", "")

            hours_worked = float(user_input)
            return hours_worked
        
        except ValueError:
            continue

def add_to_employees(employee_name, hours_worked):

    if employee_name in employees:
        return False
    else:
        employees[employee_name] = hours_worked

def calculate_overtime():
    for name, hours in employees.items():
        if hours > 8:
            overtime = hours - 8
            overtimes[name] = overtime

def summary():
    print("The employees and their worked hours:")
    for key, values in employees.items():
        print(f"- {key}: {values:.1f} h")

    print(
        "Employees who worked overtime and their overtime hours:"
        )
    for key, values in overtimes.items():
        print(f"- {key}: {values:.1f} h")

def main():
    while True:
        employee_name = get_employe_name()
        if employee_name is None:
            break
        else:
            hours_worked = get_hours_worked()
            add_to_employees(employee_name, hours_worked)
            calculate_overtime()
            continue
        
    summary()

main()








      




