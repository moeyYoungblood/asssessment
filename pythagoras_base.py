#pythagoras equation generator + number questions for pythagoras
#random number generator
import random
# define users choice and gives us random numbers
random_num1 = random.randint(3, 13)
random_num2 = random.randint(3, 13)
user_choice = ("1", "2", "3")

# a^2 + b^2 = c^2, c^2 + a^2 = b^2, c^2 + b^2 = a^2 questions
a_squared = [random_num1 * random_num1]
b_squared = [random_num2 * random_num2]
c_squared = [a_squared + b_squared]
if user_choice == "1":
    response = float(input(f"{a_squared} + {b_squared} = "))
    correct_answer = c_squared = a_squared + b_squared
if user_choice == "2":
    response = float(input(f"{c_squared} - {a_squared} = "))
    correct_answer = b_squared = c_squared - a_squared
if user_choice == "3":
    response = float(input(f"{c_squared} - {b_squared} = "))
    correct_answer = a_squared = c_squared - b_squared


def int_checker(question):
    error = "Please enter a valid number."

    while True:
        try:
            if question == "1":
            if response == int(response):
                print("Correct answer!")
            else:
                print(f"Incorrect answer! You said {response}, but the correct answer is {correct_answer} ")
            break

        except ValueError:
            print(error)






