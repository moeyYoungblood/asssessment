import random

# define users choice and gives us random numbers
random_num1 = random.randint(3, 13)
random_num2 = random.randint(3, 13)

# a^2 + b^2 = c^2, c^2 - a^2 = b^2, c^2 - b^2 = a^2 generator
a_squared = random_num1 * random_num1
b_squared = random_num2 * random_num2
c_squared = a_squared + b_squared

# int checker (checks users enter numbers between 1-4, prints question, allows user to choose a question, checks for the correct answer
def int_checker():
    error = "Please enter a valid number."

    print("CHOOSE BETWEEN NUMBERS 1 to 4")
    print("1. a^2 + b^2 = c^2")
    print("2. c^2 - a^2 = b^2")
    print("3. c^2 - b^2 = a^2")
    print("4. random question")

    user_choice = input("Enter 1, 2, or 3 or 4: ")

    if user_choice == "1":
        question = f"{a_squared} + {b_squared} = "
        correct_answer_1 = c_squared
    elif user_choice == "2":
        question = f"{c_squared} - {a_squared} = "
        correct_answer_2 = b_squared
    elif user_choice == "3":
        question = f"{c_squared} - {b_squared} = "
        correct_answer_3 = a_squared
    elif user_choice == "4":
        question = f"{a_squared}/(a^2) - {b_squared}/(b^2) = " or f"{c_squared}/(c^2) - {a_squared}/(c^2) = " or f"{c_squared}/(c^2) - {b_squared}/(b^2) = "
        correct_answer_1 = c_squared
        correct_answer_2 = b_squared
        correct_answer_3 = a_squared

    else:
        print("Please choose 1, 2, or 3.")
        return

    while True:
        try:
            response = float(input(question))

            if response == correct_answer_1 or response == correct_answer_2 or response == correct_answer_3:
                print("Correct answer!")
            else:
                print(f"Incorrect answer! You said {response}, but the correct answer is {correct_answer_1 or correct_answer_2 or correct_answer_3}")
            break

        except ValueError:
            print(error)


int_checker()
