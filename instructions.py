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


def instructions():
    print('''
                                     ***  INSTRUCTIONS  ***
                    
To begin the Quiz, choose your difficulty level (easy 3 - 6, medium 7- 10, hard 11 - 15 or extremely hard 16-20)
Then choose the amount of questions you'd like.
If you want an infinite number of questions
press <enter> for infinite mode and type done at the end of the question where you would like to finish.
If not choose how many questions you would like to answer in the quiz.
Which will then let you choose what type of questions you want.

THEN YOUR QUIZ WILL BEGIN.
(if you're entering your answer in a square rooted format, round decimals to 2 d.p)
Good luck.

   ''')


print("🧮WELCOME TO MY PYTHAGORAS QUIZ🧮")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

#check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()