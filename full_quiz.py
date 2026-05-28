import math
import random


# Fixed quiz data stays at the top so it is easy to change later.
# Each difficulty stores: menu number: (name, lowest number, highest number).
DIFFICULTIES = {
    1: ("Easy", 1, 7),
    2: ("Medium", 8, 13),
    3: ("Hard", 14, 20),
}

# Build the difficulty menu text from the difficulty data above.
DIFFICULTY_OPTIONS = {
    number: f"{name} ({low}-{high})"
    for number, (name, low, high) in DIFFICULTIES.items()
}

# These are the question types the user can choose.
QUESTION_OPTIONS = {
    1: "Find c²",
    2: "Find b²",
    3: "Find a²",
    4: "Random question",
}

# Messages shown at the end depending on the user's score.
RESULT_MESSAGES = {
    "excellent": "Great job! you got EXCELLENCE!!!!",
    "merit": "Good effort. You got a Merit",
    "achieved": "Keep practising. You got Achieved",
    "not achieved": "Keep practising. You got Not Achieved",
}


def heading(title):
    """Print a title with divider lines above and below it."""
    print()
    print("=" * 50)
    print(title)
    print("=" * 50)


def str_checker(question, valid_answers):
    """Check word answers such as yes/no and allow their first letters."""
    error = f"Please enter one of these options: {valid_answers}"

    while True:
        response = input(question).lower().strip()

        for valid_answer in valid_answers:
            if response == valid_answer or response == valid_answer[0]:
                return valid_answer

        print(error)
        print()


def num_check(
    question,
    low=None,
    high=None,
    exit_code=None,
    allow_decimal=False,
    correct_answer=None,
    root_answer=None,
):
    """Ask for a number, check limits, and optionally mark a quiz answer."""
    if low is None and high is None:
        error = "Please enter a valid number."
    elif high is None:
        error = f"Please enter a number that is {low} or higher."
    else:
        error = f"Please enter a number from {low} to {high}."

    while True:
        response = input(question).lower().strip()

        if exit_code is not None and response == exit_code:
            return exit_code

        try:
            # Answers use floats so square root answers like 6.4 can be accepted.
            response = float(response) if allow_decimal else int(response)

            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                # When correct_answer is given, num_check also marks the quiz answer.
                if correct_answer is not None and root_answer is not None:
                    rounded_answer = round(response, 2)
                    rounded_correct = round(correct_answer, 2)
                    rounded_root = round(root_answer, 2)
                    answer_text = f"{rounded_correct} or {rounded_root}"

                    if rounded_answer in (rounded_correct, rounded_root):
                        print("Correct answer!")
                        return 1, answer_text, str(response)

                    print("Incorrect")
                    return 0, answer_text, str(response)

                return response
        except ValueError:
            print(error)


def menu_choice(title, options):
    """Show a numbered menu and return the user's chosen number."""
    heading(title)

    # Print every option from the dictionary.
    for number, option_text in options.items():
        print(f"{number}. {option_text}")

    # min/max work because the menu numbers are consecutive.
    choice_numbers = ", ".join(str(number) for number in options)
    return num_check(f"Enter {choice_numbers}: ", min(options), max(options))


def instructions():
    """Print the quiz instructions."""
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


def choose_question_settings():
    """Ask for the question type and difficulty, then return those settings."""
    question_choice = str(menu_choice("CHOOSE A QUESTION TYPE", QUESTION_OPTIONS))
    difficulty_choice = menu_choice("CHOOSE A DIFFICULTY", DIFFICULTY_OPTIONS)
    _, lowest_number, highest_number = DIFFICULTIES[difficulty_choice]

    return question_choice, lowest_number, highest_number


def build_question(question_type, first_number, second_number):
    """Create one question, its answers, and the worked explanation."""
    a_squared = first_number ** 2
    b_squared = second_number ** 2
    c_squared = a_squared + b_squared

    # Each question type stores:
    # question text, answer, answer name, formula rule, and substituted working.
    question_data = {
        "1": (
            f"If [a²] is {first_number}² AND [b²] is {second_number}²"
            f"\nWhat is c² or √c²?  ",
            c_squared,
            "c²",
            "a² + b² = c²",
            f"{a_squared} + {b_squared}",
        ),
        "2": (
            f"If [c²] is {c_squared} AND [a²] is {first_number}²"
            f"\nWhat is b² or √b²? ",
            b_squared,
            "b²",
            "c² - a² = b²",
            f"{c_squared} - {a_squared}",
        ),
        "3": (
            f"If [c²] is {c_squared} AND [b²] is {second_number}²"
            f"\nWhat is a² or √a²? ",
            a_squared,
            "a²",
            "c² - b² = a²",
            f"{c_squared} - {b_squared}",
        ),
    }

    question, answer, answer_name, rule, working = question_data[question_type]
    root_answer = math.sqrt(answer)

    # This is saved so the user can see how to do wrong questions later.
    explanation = (
        f"Step 1: Use the rule {rule}\n"
        f"Step 2: Substitute the values: {working}\n"
        f"Step 3: Work it out: {answer}\n"
        f"Step 4: So {answer_name} = {answer}\n"
        f"Step 5: If you want the square root answer, √{answer} = {round(root_answer, 2)}"
    )

    return question, answer, root_answer, explanation


def make_question(lowest_number, highest_number, user_choice):
    """Choose random numbers and build a fresh question for one round."""
    first_number = random.randint(lowest_number, highest_number)
    second_number = random.randint(lowest_number, highest_number)

    # Random mode chooses a new question type each round.
    if user_choice == "4":
        user_choice = random.choice(["1", "2", "3"])

    return build_question(user_choice, first_number, second_number)


def num_questions():
    """Ask how many questions the user wants, or start infinite mode."""
    heading("CHOOSE NUMBER OF QUESTIONS")

    question_amount = num_check(
        "Press enter for infinite mode, or type how many questions you want: ",
        low=1,
        exit_code="",
    )

    if question_amount == "":
        return "", "infinite"

    return question_amount, "normal"


def run_quiz(lowest_number, highest_number, number_of_rounds, mode, user_choice):
    """Run all quiz questions and save each round in the quiz history."""
    quiz_history = []
    question_count = 0
    exit_code = "done"

    heading("QUIZ START")
    print(f"Question type: {QUESTION_OPTIONS[int(user_choice)]}")
    print(f"Number range: {lowest_number} to {highest_number}")
    print("Mode: Infinite" if mode == "infinite" else f"Questions: {number_of_rounds}")

    # Normal mode stops after the chosen number of questions.
    # Infinite mode keeps going until the user types done.
    while mode == "infinite" or question_count < number_of_rounds:
        if mode == "infinite":
            heading(f"QUESTION {question_count + 1}")
            print("Infinite mode")
            print(f"Type {exit_code} to finish.")
        else:
            heading(f"QUESTION {question_count + 1} OF {number_of_rounds}")

        question_text, correct_answer, root_answer, explanation = make_question(
            lowest_number, highest_number, user_choice
        )
        checked_answer = num_check(
            question_text,
            exit_code=exit_code if mode == "infinite" else None,
            allow_decimal=True,
            correct_answer=correct_answer,
            root_answer=root_answer,
        )
        print()

        # In infinite mode, done stops the quiz before checking an answer.
        if checked_answer == exit_code:
            break

        question_result, answer_text, user_answer = checked_answer

        # Save the result so it can be used for score, history, and explanations.
        quiz_history.append({
            "result": question_result,
            "answer": answer_text,
            "user_answer": str(user_answer),
            "question": question_text,
            "explanation": explanation,
        })
        question_count += 1

    return quiz_history


def calculate_result_level(total_correct, total_questions):
    """Return the final result level based on the user's score."""
    if total_questions == 0:
        return "no questions answered"
    if total_correct == total_questions:
        return "excellent"
    if total_correct >= total_questions * 0.75:
        return "merit"
    if total_correct >= total_questions * 0.5:
        return "achieved"
    return "not achieved"


def quiz_results(quiz_history):
    """Show the score and optionally print the full quiz history."""
    total_correct = sum(round_data["result"] for round_data in quiz_history)
    total_questions = len(quiz_history)
    result_level = calculate_result_level(total_correct, total_questions)

    if result_level == "no questions answered":
        heading("QUIZ FINISHED")
        print("No questions were answered.")
        return result_level

    heading("QUIZ SUMMARY")
    print(f"Score: {round((total_correct / total_questions) * 100)}% out of 100%")
    print(RESULT_MESSAGES[result_level])

    if str_checker("Do you want to see your quiz history? ", ["yes", "no"]) == "yes":
        heading("QUIZ HISTORY")

        # enumerate adds question numbers while looping through the history.
        for question_number, round_data in enumerate(quiz_history, start=1):
            print(f"Question {question_number}:")
            print(round_data["question"])
            print(f"Your answer: {round_data['user_answer']}")

            if round_data["result"] == 1:
                print("Result: Correct")
            else:
                print("Result: Incorrect")
                print(f"Correct answer: {round_data['answer']}")
            print()

    return result_level


def explain_wrong_questions(quiz_history, result_level):
    """Offer worked explanations for questions the user got wrong."""
    # Skip this if the user got all questions right or answered no questions.
    if result_level in ("excellent", "no questions answered"):
        return

    want_explanations = str_checker(
        "Would you like to know how to do the questions you got wrong? ",
        ["yes", "no"],
    )

    if want_explanations == "no":
        return

    heading("HOW TO DO THE QUESTIONS YOU GOT WRONG")

    # Only print explanations for incorrect answers.
    for question_number, round_data in enumerate(quiz_history, start=1):
        if round_data["result"] == 0:
            print(f"Question {question_number}:")
            print(round_data["question"])
            print()
            print(round_data["explanation"])
            print()


# Main routine starts here.
heading("WELCOME TO MY PYTHAGORAS QUIZ")

if str_checker("Do you want to read the instructions? ", ["yes", "no"]) == "yes":
    instructions()

while True:
    # Get the quiz setup choices.
    user_choice, lowest_number, highest_number = choose_question_settings()
    number_of_rounds, mode = num_questions()

    # Run the quiz, show results, then offer explanations for wrong answers.
    quiz_history = run_quiz(
        lowest_number, highest_number, number_of_rounds, mode, user_choice
    )
    result_level = quiz_results(quiz_history)
    explain_wrong_questions(quiz_history, result_level)

    if str_checker("Do you want to do another quiz? ", ["yes", "no"]) == "no":
        heading("QUIZ FINISHED")
        break

print()
