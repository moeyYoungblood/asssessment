
import random

# random number generator

random_num1 = random.randint(1, 10)
random_num2 = random.randint(1, 10)

# randomizes the choice of the operation being used
operation = random.choice(["+", "-", "*", "/"])
if operation == "+":
    correct_answer = random_num1 + random_num2
elif operation == "-":
    correct_answer = random_num1 - random_num2
elif operation == "*":
    correct_answer = random_num1 * random_num2
elif operation == "/":
    correct_answer = random_num1 / random_num2

# ask the user for an answer and check it + random question generator using 'operations' and random numbers with a rounding code for decimals
def int_checker():
    error = "Please enter a valid number."

    while True:
        try:
            response = float(input(f"{random_num1} {operation} {random_num2} = "))
            rounded_response = round(response, 2)
            rounded_correct_answer = round(correct_answer, 2)

            if rounded_response == rounded_correct_answer:
                print("Correct answer!")
            else:
                print(f"Incorrect answer! You said {response}, but the correct answer is {correct_answer}")
            break

        except ValueError:
            print(error)


int_checker()
