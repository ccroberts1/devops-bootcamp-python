import random

def random_number_guess():
    try:
        user_input = ""
        correct_num = random.randint(1,9)
        while user_input != "exit":
            user_input = input("Guess a number between 1 and 9\n")
            if user_input !="exit":
                user_guess = int(user_input)
                if user_guess < correct_num:
                    print("Your guess is too low")
                elif user_guess > correct_num:
                    print("Your guess is too high")
                elif user_guess == correct_num:
                    print("You won!")
                    user_input = "exit"
                else:
                    print("You did not provide a valid number")
    except Exception as e:
        print(e)
        print("Your input is not in a valid format")