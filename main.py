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


