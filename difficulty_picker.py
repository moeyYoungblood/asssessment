import random
# lets users choose a difficulty in the quiz
def choose_difficulty():
    # prints the difficulty levels and tells them how difficult each difficult is.
    print("Choose a difficulty:")
    print("1. (Easy numbers 3- 6)")
    print("2. (Medium numbers 7 - 10)")
    print("3. Hard (numbers 11 - 20)")
    #     lets users input a difficulty
    while True:
        difficulty = input("Enter easy, medium, or hard: ")

        if difficulty == "easy":
            return 3, 6
        elif difficulty == "medium":
            return 7, 10
        elif difficulty == "hard":
            return 11, 15
        else:
            print("Please choose a difficulty.")

# define users choice and gives us random numbers
low, high = choose_difficulty()
random_num1 = random.randint(low, high)
random_num2 = random.randint(low, high)