import random
import math


answer_history = []

# check users enter yes (y) or no (n)
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase

        user_response = input(question).lower()

        for item in valid_ans:

            # check if the user response is a word in the list

            if item == user_response:

                return item

            # check if the user response is the same as

            # the first letter of an item in the list

            elif user_response == item[0]:

                return item

        # print error if user does not enter something that is valid

        print(error)

        print()

# yes/no checker
def yes_no(questions):
    while True:
        response = input(questions).lower()

        # check if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please respond with yes / no")

# displays the instructions for the users
def instructions():
    print('''
                                     ***  INSTRUCTIONS  ***

To begin the Quiz, choose what type of question you would like.
Which will allow you to choose your difficulty level (easy 3 - 6, medium 7- 10, hard 11 - 15 or extremely hard 16-20)
Then choose the amount of questions you'd like.
If you want an infinite number of questions
Press <enter> for infinite mode and type done when you want to finish.
If not choose how many questions you would like to answer in the quiz.


THEN YOUR QUIZ WILL BEGIN.
(if you're entering your answer in a square rooted format, round decimals to 2 d.p)
Good luck.

   ''')

# allows users to be able to choose a difficulty
# four difficulties given.
def choose_difficulty():
    # prints the difficulty levels and tells them how difficult each difficult is.
    print(f"Choose a difficulty:"
    f"\n"    
    f"\n1. (Easy numbers 3- 6)"
    f"\n2. (Medium numbers 7 - 10)"
    f"\n3. Hard (numbers 11 - 15)"
    f"\n4. Extremely hard (numbers 16 - 20)")
    #     lets users input a difficulty
    while True:
        difficulty = input(f"\nEnter (1)easy, (2)medium, (3)hard or (4)extremely hard: ")
        # sets the parameters for each difficulty
        if difficulty == "easy" or difficulty == "1":
            return 3, 6
        elif difficulty == "medium" or difficulty == "2":
            return 7, 10
        elif difficulty == "hard" or difficulty == "3":
            return 11, 15
        elif difficulty == "extremely hard" or difficulty == "4":
            return 16, 20
        else:
            print("Please choose a difficulty.")

# int checker (checks users enter numbers between 1-4, prints question,
# allows user to choose a question, checks for the correct answer) + adds a function where the numbers are represented as number^2
# allows user to enter a number square rooted or squared
def choose_question():
    # lets the user pick what type of question they want
    error = "Please enter a valid number."
    #  prints choices the user has
    print("CHOOSE BETWEEN NUMBERS 1 to 4")
    print("1. FIND c^2")
    print("2. FIND b^2")
    print("3. FIND a^2")
    print("4. RANDOM QUESTION")

    # gives user a choice between the questions
    while True:
        user_choice = input("Enter 1, 2, 3, or 4: \n")
        if user_choice in ["1", "2", "3", "4"]:
            return user_choice
        print(error)

def make_question(low, high, user_choice):
    random_num1 = random.randint(low, high)
    random_num2 = random.randint(low, high)

    # a^2 + b^2 = c^2, c^2 - a^2 = b^2, c^2 - b^2 = a^2 generator
    a_squared = random_num1 * random_num1
    b_squared = random_num2 * random_num2
    c_squared = a_squared + b_squared


    if user_choice == "1":
        question = (f""
                    f"If A squared is {random_num1}^2 and B squared is {random_num2}^2. "
                    f"What is the C squared? ")
        correct_answer = c_squared
        correct_answer_2 = math.sqrt(c_squared)
    elif user_choice == "2":
        question = (f""
                    f"If C squared is {c_squared} and A squared is {random_num1}^2. "
                    f"What is B^2? ")
        correct_answer = b_squared
        correct_answer_2 = math.sqrt(b_squared)
    elif user_choice == "3":
        question = (f""
                    f"If C squared is {c_squared} and B squared is {random_num2}^2. "
                    f"What is A^2? ")
        correct_answer = a_squared
        correct_answer_2 = math.sqrt(a_squared)
    elif user_choice == "4":
        random_question = random.choice(["1", "2", "3"])


        # allows the code to be able to choose a random question
        # allows random question to be presented as ^2 (was not being presented as ^2 and code was being glitched without it)
        if random_question == "1":
            question = (f""
                        f"If A squared is {random_num1}^2 and B squared is {random_num2}^2. "
                        f"What is the C squared? ")
            correct_answer = c_squared
            correct_answer_2 = math.sqrt(c_squared)

        elif random_question == "2":
            question = (f""
                        f"If C squared is {c_squared} and A squared is {random_num1}^2. "
                        f"What is B^2? ")
            correct_answer = b_squared
            correct_answer_2 = math.sqrt(b_squared)

        else:
            question = (f""
                        f"If C squared is {c_squared} and B squared is {random_num2}^2. "
                        f"What is A^2? ")
            correct_answer = a_squared
            correct_answer_2 = math.sqrt(a_squared)

    else:
        print("Please choose a type of question, 1, 2, 3, or 4.")
        return None

    return question, correct_answer, correct_answer_2


def int_checker(question, correct_answer, correct_answer_2, mode, exit_code):

    # checks user enters a correct answer
    while True:
        try:
            response = input(question).lower().strip()

            if mode == "infinite" and response == exit_code:
                return "exit"

            # allows users to be able to enter a decimal answer
            response = float(response)
            # allows users to enter a rounded number and ot break the code.
            rounded_response = round(response, 2)
            rounded_correct_answer = round(correct_answer, 2)
            rounded_correct_answer_2 = round(correct_answer_2, 2)

            # prints if the user got the answer correct or incorrect
            if rounded_response == rounded_correct_answer:
                print("Correct answer!")
                answer_history.append(f"{round(correct_answer, 2)} or {round(correct_answer_2, 2)}")
                return 1
            elif rounded_response == rounded_correct_answer_2:
                print("Correct answer!")
                answer_history.append(f"{round(correct_answer, 2)} or {round(correct_answer_2, 2)}")
                return 1
            #     tell the user if their incorrect with the correct answer
            else:
                print("Incorrect")
                answer_history.append(f"{round(correct_answer, 2)} or {round(correct_answer_2, 2)}")
                return 0
        except ValueError:
            print("Please enter a valid number.")
            print()

# lets the user pick their desired amounts of questions or do the quiz infinitely
def num_questions():
    while True:
        num_questions = input(
            "Press enter if you would like infinite mode. "
            "If not, how many questions would you like? "
        )

        if num_questions == "":
            return "", "infinite"

        try:
            num_questions = int(num_questions)
            if num_questions > 0:
                return num_questions, "normal"
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")
            print("Please enter a whole number.")

# allows infinite mode

def rounds_infinite(low, high, num_questions, mode, user_choice):
    questions_answered = 0
    history = []
    exit_code = "done"

    # lets user pick infinite mode
    while mode == "infinite" or questions_answered < num_questions:
        if mode == "infinite":
            rounds_heading = f"\nRound {questions_answered + 1} (Infinite Mode)"
            print(f"{rounds_heading} - type {exit_code} to finish")
        else:
            rounds_heading = f"\nRound {questions_answered + 1} of {num_questions}"
            print(rounds_heading)

        question, correct_answer, correct_answer_2 = make_question(low, high, user_choice)
        round_result = int_checker(question, correct_answer, correct_answer_2, mode, exit_code)

        if round_result == "exit":
            break

        history.append(round_result)
        questions_answered += 1

    return history

# gives quiz results
def quiz_results(history):
    if len(history) == 0:
        print("No questions were answered.")
        return
    # asks user if they want the game history
    see_history = string_checker("Do you want the quiz results?")
    # this piece of code is to show how the code will be presented depending on whether the user got the question right or wrong
    if see_history == "yes":
        print("\n*** QUIZ RESULTS ***")
        # what will be presented in the list of the quiz results if the user got the question right
        for count, item in enumerate(history, start=1):
            if item == 1:
                print(f"QUESTION {count}: correct")
            # what will be presented in the list of the quiz results if the user got the question wrong
            # also shows the correct answer for the user.
            else:
                print(f"QUESTION {count}: incorrect")
                print(f"Correct answer: {answer_history[count - 1]}")
        # prints the final score depending on how many questions the user asks for
        print()
        print(f"Score: {sum(history)}/{len(history)}")

    else:
        print("no history shown.")


# welcomes the user to the quiz
print("🧮WELCOME TO MY PYTHAGORAS QUIZ🧮")
print()
# asks the user whether they want instructions or not
want_instructions = yes_no("Do you want to read the instructions? ")

# presents the instrustions when the user says yes
if want_instructions == "yes":
    instructions()

user_choice = choose_question()
low, high = choose_difficulty()
num_questions, mode = num_questions()
history = rounds_infinite(low, high, num_questions, mode, user_choice)
quiz_results(history)
