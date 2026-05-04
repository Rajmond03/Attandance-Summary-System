employees = {}
overtimes = {}

def get_employee_name():
    while True:
        employee_name = input(
            "Please enter the name (end with 'done'): "
            ).strip().lower()
        
        if employee_name == "done":
            return None
        
        elif not employee_name.replace(" ", "").isalpha():
            print(
                "Only letters and spaces are allowed!"
                )
            continue
        
        else:
            return employee_name
        
def get_hours_worked():
    while True:
        try:
            user_input = input(
                "Please enter the hours worked: "
            ).replace(",", ".").replace(" ", "")

            if user_input == "":
                print(
                    "Hours worked cannot be empty!"
                    )
                continue

            hours_worked = float(user_input)
            
            if hours_worked < 1:
                print(
                    "Only positive numbers are allowed!"
                    )
                continue

            elif hours_worked > 16:
                print("Maximum overtime is 16 hours!")
                continue

            return hours_worked

        except ValueError:
            print("Only numbers are allowed!")
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
        print(
            "The employees and their worked hours:"
            )
        for key, values in employees.items():
            print(f"- {key}: {values:.1f} h")

        print(
            "Employees who worked overtime "
            "and their overtime hours:"
            )
        for key, values in overtimes.items():
            print(f"- {key}: {values:.1f} h")

def main():
    while True:
        employee_name = get_employee_name()
        if employee_name is None and not employees:
            print("No name entered!")
            continue

        elif employee_name is None:
            break

        hours_worked = get_hours_worked()
        addition = add_to_employees(employee_name, hours_worked)

        if addition is False:
            print("This name already exists!")
            continue

    calculate_overtime()    
    summary()
               
main()








      




