def calculate_operation():
    try:
        user_input = ""
        calculation_count = 0
        while user_input != "exit":
            user_input = input("Please provide two numbers and the operation you want to perform on them in a comma separated list in the order you want to perform the operation\n Possible operations: add, subtract, multiply and divide\n")
            if user_input !="exit":
                user_input_list = user_input.split(",")
                num_one = int(user_input_list[0])
                num_two = int(user_input_list[1])
                operation = user_input_list[2]
                if operation == "add":
                    print(num_one + num_two)
                    calculation_count += 1
                elif operation == "subtract":
                    print(num_one - num_two)
                    calculation_count += 1
                elif operation == "multiply":
                    print(num_one * num_two)
                    calculation_count += 1
                elif operation == "divide":
                    print(num_one / num_two)
                    calculation_count += 1
                else:
                    print("You did not provide a valid operation")
            if user_input == "exit":
                print(f"You have completed {calculation_count} calculation(s)")
    except Exception as e:
        print(e)
        print("Your input is not in a valid format")