def working_with_lists(num_list):
    ten_or_over_list = []
    user_input = input("Enter a number and I'll find any higher number(s) in the list\n")

    for num in num_list:
        if num > int(user_input):
            ten_or_over_list.append(num)

    print(ten_or_over_list)


def dictionaries_employee(employee):
    for key, value in employee.items():
        print(f"{key}:{value}")


def working_with_dictionaries(dict_one, dict_two):

    dict_two.update(dict_one)

    # sum_of_values = 0
    # for key, value in dict_two.items():
    #     sum_of_values = sum_of_values + value

    max_value = max(dict_two.values())
    print(max_value)
    min_value = min(dict_two.values())
    print(min_value)


def list_of_dictionaries(provided_list):
    for item in provided_list:
        print(f"\nName: {item['name']} \nJob: {item['job']} \nCity: {item['address']['city']}")

    print(list[1]["address"]["country"])
