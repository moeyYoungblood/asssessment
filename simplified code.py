import math
import random


# prints a divider line to make the quiz easier to read
def line():
    print("=" * 50)


# prints a heading with lines above and below it
def heading(title):
    print()
    line()
    print(title)
    line()


# This function is used for menu-style inputs.
# It keeps asking the user until they type one of the allowed answers.
# It also accepts either the full word or the first letter.
# Example:
# valid_answers = ["yes", "no"]
# The user can type:
# yes / y / no / n
def choice_checker(question, valid_answers):
    error = f"Please enter one of these options: {valid_answers}"

    while True:
        response = input(question).lower().strip()
        matched_answer = None

        # Check every valid answer in the list.
        # If the user types the full answer or its first letter,
        # return that answer back to the program.
        for valid_answer in valid_answers:
            if response == valid_answer or response == valid_answer[0]:
                matched_answer = valid_answer
                break

        if matched_answer is not None:
            return matched_answer

        print(error)
        print()


# This function prints the instructions for the quiz.
# It explains:
# 1. how to start
# 2. how infinite mode works
# 3. how to round decimal answers
def instructions():
    heading("INSTRUCTIONS")
    print("""

1. Choose the type of question.
2. Choose the difficulty.
3. Choose how many questions you want.
4. If you use infinite mode, type done to finish.

You can type either:
- the squared answer
- or the square root answer ("√" means square root)

if answering in square root, round decimal answers to 2 decimal places.
Good luck.
""")


# lets the user choose a difficulty and returns the matching number range
def choose_difficulty():
    # A dictionary is used here to keep the code shorter.
    # The key is what the user types.
    # The value is the low and high number range for that difficulty.
    difficulty_data = {
        "1": (3, 6),
        "easy": (3, 6),
        "2": (7, 10),
        "medium": (7, 10),
        "3": (11, 15),
        "hard": (11, 15),
        "4": (16, 20),
        "extremely hard": (16, 20),
    }

    heading("CHOOSE A DIFFICULTY")
    print("1. Easy (3-6)")
    print("2. Medium (7-10)")
    print("3. Hard (11-15)")
    print("4. Extremely hard (16-20)")

    while True:
        difficulty_choice = input("\nEnter 1, 2, 3, or 4: ").lower().strip()

        if difficulty_choice in difficulty_data:
            lowest_number, highest_number = difficulty_data[difficulty_choice]
            return lowest_number, highest_number

        print("Please choose a difficulty.")


# This function lets the user choose the type of question
# they want for the whole quiz.
# The user picks one of four options:
# 1. find c^2
# 2. find b^2
# 3. find a^2
# 4. random question each round
def choose_question():
    heading("CHOOSE A QUESTION TYPE")
    print("1. Find c²")
    print("2. Find b²")
    print("3. Find a²")
    print("4. Random question")

    return choice_checker("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"])


# This function builds one Pythagoras question.
# It takes:
# - question_type: which version of the question to ask
# - first_number and second_number: the numbers that make the triangle
#
# It works out:
# a^2, b^2, and c^2
#
# Then it returns:
# - the question text to show the user
# - the squared answer
# - the square root version of the answer
#
# The second answer is included because your quiz accepts
# both the squared form and the rooted form.
def build_question(question_type, first_number, second_number):
    a_squared = first_number ** 2
    b_squared = second_number ** 2
    c_squared = a_squared + b_squared

    if question_type == "1":
        question = (f"If [a²] is {first_number}² AND [b²] is {second_number}²"
                    f"\nWhat is c² or √c²?  ")
        explanation = (
            f"Step 1: Use the rule a² + b² = c²\n"
            f"Step 2: Substitute the values: {a_squared} + {b_squared}\n"
            f"Step 3: Add them together: {c_squared}\n"
            f"Step 4: So c² = {c_squared}\n"
            f"Step 5: If you want the square root answer, √{c_squared} = {round(math.sqrt(c_squared), 2)}"
        )
        return question, c_squared, math.sqrt(c_squared), explanation

    if question_type == "2":
        question = (f"If [c²] is {c_squared} AND [a²] is {first_number}²"
                    f"\nWhat is b² or √b²? ")
        explanation = (
            f"Step 1: Use the rule c² - a² = b²\n"
            f"Step 2: Substitute the values: {c_squared} - {a_squared}\n"
            f"Step 3: Subtract them: {b_squared}\n"
            f"Step 4: So b² = {b_squared}\n"
            f"Step 5: If you want the square root answer, √{b_squared} = {round(math.sqrt(b_squared), 2)}"
        )
        return question, b_squared, math.sqrt(b_squared), explanation

    question = (f"If [c²] is {c_squared} AND [b²] is {second_number}²"
                f"\nWhat is a² or √a²? ")
    explanation = (
        f"Step 1: Use the rule c² - b² = a²\n"
        f"Step 2: Substitute the values: {c_squared} - {b_squared}\n"
        f"Step 3: Subtract them: {a_squared}\n"
        f"Step 4: So a² = {a_squared}\n"
        f"Step 5: If you want the square root answer, √{a_squared} = {round(math.sqrt(a_squared), 2)}"
    )
    return question, a_squared, math.sqrt(a_squared), explanation


# This function makes a fresh question for each round.
# First it creates two random numbers inside the chosen difficulty range.
# Then:
# - if the user picked a fixed question type, it uses that
# - if the user picked random, it chooses 1, 2, or 3 at random
#
# After that, it sends the values to build_question()
# and returns the finished question data.
def make_question(lowest_number, highest_number, user_choice):
    first_number = random.randint(lowest_number, highest_number)
    second_number = random.randint(lowest_number, highest_number)

    # if the user picked random mode, choose a question type for this round
    if user_choice == "4":
        user_choice = random.choice(["1", "2", "3"])

    return build_question(user_choice, first_number, second_number)


# turns the question number choice into readable text for the quiz summary
def question_type_name(user_choice):
    names = {
        "1": "Find c^2",
        "2": "Find b^2",
        "3": "Find a^2",
        "4": "Random question",
    }
    return names[user_choice]


# This function checks the user's answer.
# It is responsible for:
# - asking the question
# - stopping infinite mode if the user types the exit code
# - checking if the answer is correct
# - returning the result
#
# It returns:
# - "exit", None if the user wants to stop infinite mode
# - 1, answer_text if the answer is correct
# - 0, answer_text if the answer is incorrect
def int_checker(question, correct_answer, second_answer, mode, exit_code):
    while True:
        response = input(question).lower().strip()

        # In infinite mode, the user can leave by typing the exit code
        # instead of typing a number answer.
        if mode == "infinite" and response == exit_code:
            return "exit", None

        try:
            response = float(response)

            # Round everything to 2 decimal places so that
            # small decimal differences do not cause unfair marking.
            rounded_response = round(response, 2)
            rounded_correct = round(correct_answer, 2)
            rounded_root_answer = round(second_answer, 2)

            # The answer counts as correct if it matches either
            # the squared answer or the square root answer.
            if rounded_response == rounded_correct or rounded_response == rounded_root_answer:
                print("Correct answer!")
                return 1, f"{rounded_correct} or {rounded_root_answer}"

            print("Incorrect")
            return 0, f"{rounded_correct} or {rounded_root_answer}"

        except ValueError:
            print("Please enter a valid number.")
            print()


# This function asks how many questions the user wants.
# If they press enter without typing a number,
# the program switches to infinite mode.
# Otherwise, it checks that the number is a whole number
# greater than zero.
def num_questions():
    heading("CHOOSE NUMBER OF QUESTIONS")
    while True:
        question_amount = input("Press enter for infinite mode, or type how many questions you want: ").strip()

        # pressing enter puts the quiz into infinite mode
        if question_amount == "":
            return "", "infinite"

        try:
            question_amount = int(question_amount)
            if question_amount > 0:
                return question_amount, "normal"
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")


# This is the main quiz loop.
# It keeps the quiz running round by round.
#
# It stores two lists:
# - history: saves 1 for correct and 0 for incorrect
# - answer_history: saves the correct answer text for each round
#
# At the end, both lists are returned so the results function
# can show the final summary.
def run_quiz(lowest_number, highest_number, number_of_rounds, mode, user_choice):
    answer_history = []
    question_result_history = []
    question_text_history = []
    worked_explanation_history = []
    question_count = 0
    infinite_mode_exit_code = "done"

    heading("QUIZ START")
    print(f"Question type: {question_type_name(user_choice)}")
    print(f"Number range: {lowest_number} to {highest_number}")
    if mode == "infinite":
        print("Mode: Infinite")
    else:
        print(f"Questions: {number_of_rounds}")

    # Keep looping until:
    # - the user has answered all normal-mode questions, or
    # - the user exits infinite mode
    while mode == "infinite" or question_count < number_of_rounds:
        if mode == "infinite":
            heading(f"QUESTION {question_count + 1}")
            print("Infinite mode")
            print(f"Type {infinite_mode_exit_code} to finish.")
        else:
            heading(f"QUESTION {question_count + 1} OF {number_of_rounds}")

        # Build the next question, then check the user's answer.
        question_text, correct_answer, second_answer, worked_explanation = make_question(
            lowest_number, highest_number, user_choice
        )
        question_result, answer_text = int_checker(
            question_text,
            correct_answer,
            second_answer,
            mode,
            infinite_mode_exit_code,
        )
        print()

        # If the user typed the exit code, stop the quiz straight away.
        if question_result == "exit":
            break

        # Save the score result and correct answer for this round.
        question_result_history.append(question_result)
        answer_history.append(answer_text)
        question_text_history.append(question_text)
        worked_explanation_history.append(worked_explanation)
        question_count += 1

    return (
        question_result_history,
        answer_history,
        question_text_history,
        worked_explanation_history,
    )


# This function prints the final results of the quiz.
# It can:
# - tell the user if no questions were answered
# - ask if they want to see the results
# - show which questions were right or wrong
# - show the final score
def quiz_results(question_result_history, answer_history, question_text_history):
    if len(question_result_history) == 0:
        heading("QUIZ FINISHED")
        print("No questions were answered.")
        return "no questions answered"

    show_results = choice_checker("Do you want to see the quiz results? ", ["yes", "no"])

    # even if the user skips the visible results, still work out
    # the level so the explanation section can behave properly
    if show_results == "no":
        total_correct = sum(question_result_history)
        total_questions = len(question_result_history)

        if total_correct == total_questions:
            return "excellent"
        elif total_correct >= total_questions * 0.75:
            return "merit"
        elif total_correct >= total_questions * 0.5:
            return "achieved"
        else:
            return "not achieved"

    heading("QUIZ RESULTS")
    total_correct = sum(question_result_history)
    total_questions = len(question_result_history)

    for question_number, question_result in enumerate(question_result_history, start=1):
        print(f"Question {question_number}:")
        print(question_text_history[question_number - 1])
        if question_result == 1:
            print("Result: Correct")
        else:
            print("Result: Incorrect")
            print(f"Correct answer: {answer_history[question_number - 1]}")
        print()

    print(f"Score: {total_correct}/{total_questions}")

    if total_correct == total_questions:
        print("Great job! you got EXCELLENCE!!!!")
        return "excellent"
    elif total_correct >= total_questions * 0.75:
        print("Good effort. You got a Merit")
        return "merit"
    elif total_correct >= total_questions * 0.5:
        print("Keep practising. You got achieved")
        return "achieved"
    else:
        print("Keep practising.You got Not Achieved")
        return "not achieved"


def explain_wrong_questions(question_result_history, question_text_history, worked_explanation_history, result_level):
    # users who got everything right do not need the worked solutions
    if result_level == "excellent":
        return

    want_explanations = choice_checker(
        "Would you like to know how to do the questions you got wrong? ",
        ["yes", "no"]
    )

    if want_explanations == "no":
        return

    heading("HOW TO DO THE QUESTIONS YOU GOT WRONG")

    wrong_found = False

    for question_number, question_result in enumerate(question_result_history, start=1):
        if question_result == 0:
            wrong_found = True
            print(f"Question {question_number}:")
            print(question_text_history[question_number - 1])
            print()
            print(worked_explanation_history[question_number - 1])
            print()

    if not wrong_found:
        print("You did not get any questions wrong.")


# Main routine starts here
# The order is:
# 1. welcome message
# 2. ask if the user wants instructions
# 3. choose question type
# 4. choose difficulty
# 5. choose amount of questions
# 6. run the quiz
# 7. show results
heading("WELCOME TO MY PYTHAGORAS QUIZ")

want_instructions = choice_checker("Do you want to read the instructions? ", ["yes", "no"])

if want_instructions == "yes":
    instructions()

while True:
    # Ask the user what kind of quiz they want to do.
    user_choice = choose_question()
    lowest_number, highest_number = choose_difficulty()
    number_of_rounds, mode = num_questions()

    # Run the quiz and get back four lists:
    # 1. whether each answer was right or wrong
    # 2. the correct answers for each question
    # 3. the text of each question
    # 4. the worked explanations for each question
    question_result_history, answer_history, question_text_history, worked_explanation_history = run_quiz(
        lowest_number, highest_number, number_of_rounds, mode, user_choice
    )

    # Show the quiz results and store the final level
    # such as excellence, merit, achieved, or not achieved.
    result_level = quiz_results(
        question_result_history,
        answer_history,
        question_text_history,
    )

    # Work out if the user should be offered the explanations section.
    should_show_explanations = result_level in [
        "merit",
        "achieved",
        "not achieved",
    ]

    # If the result was not excellence, offer to show
    # how to do the questions they got wrong.
    if should_show_explanations:
        explain_wrong_questions(
            question_result_history,
            question_text_history,
            worked_explanation_history,
            result_level,
        )

    play_again = choice_checker("Do you want to do another quiz? ", ["yes", "no"])

    if play_again == "no":
        heading("QUIZ FINISHED")
        break

print()
