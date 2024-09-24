def find_youngest_employee(employee_list):
    youngest_age = employee_list[0]["age"]
    youngest_name = employee_list[0]["name"]

    for employee in employee_list:
        if employee["age"] < youngest_age:
            youngest_age = employee["age"]
            youngest_name = employee["name"]

    print(f"Youngest Employee\n Name: {youngest_name}\n Age:{youngest_age}")

def upper_and_lower_calculator(string):
    num_of_lower = sum(1 for char in string if char.islower())
    num_of_upper = sum(1 for char in string if char.isupper())

    print(f"Number of lower-case letters: {num_of_lower}")
    print(f"Number of upper-case letters: {num_of_upper}")

def find_even_num(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    print(even_list)