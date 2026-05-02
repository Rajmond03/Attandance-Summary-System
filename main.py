employees = {}
overtime_workers = {}

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








      




