import random




questions = 5
Incorrect_answer = 0
questions_answered = 0
Correct_Answer = 0
# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low= None, high=None, exit_code= "xxx"):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
            print(error)

    # checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

print("➕➖ Welcome to the Math Quiz ✖️➗")
print()

want_instructions = yes_no("Do you want to read the instructions? ")
# Ask user for number of rounds / infinite mode

num_rounds = int_check("Rounds <enter for infinite mode.: ",
                       low=1, exit_code="xxx")


if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

def instruction():
    print('''

**** Instructions ****

To begin, choose the number of rounds and try to get as many math questions you answer correct.

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to try to get as many math questions as possible right

 Good luck.      

    ''')

difficulty = input("Choose difficulty (easy, medium or hard): ").lower()

# operations and number range based on difficulty
if difficulty == "easy":
    operations = ["+", "-"]
    low, high = 1, 10
elif difficulty == "medium":
    operations = ["+", "-", "*", "/"]
    low, high = 1, 20
else:
    operations = ["+", "-", "*", "/"]
    low, high = 10, 100


# Game loop starts here
while True:
    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ Round {questions_answered + 1} (Infinite Mode) ♾♾♾"
    else:
        rounds_heading = f"\n💿💿💿 Round {questions_answered + 1} of {num_rounds} 💿💿💿"

    random_operation = random.choice(operations)

    # Generate numbers
    if random_operation == "/":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        question_num = num1 * num2
        answer = num1
    else:
        num1 = random.randint(low, high)
        num2 = random.randint(low, high)
        question_num = num1
        answer = eval(f"{num1} {random_operation} {num2}")

    # Show the questions
    if random_operation == "/":
        user_answer = int(input(f"\nWhat is {question_num} {random_operation} {num2}? "))
    else:
        user_answer = int(input(f"\nWhat is {num1} {random_operation} {num2}? "))

    # Check the answer
    if user_answer == answer:
        print("Correct!")
        Correct_Answer += 1
        questions_answered += 1
    else:
        print(f"Wrong! The answer was {answer}")
        Incorrect_answer += 1
        questions_answered += 1

        # if users are in infinite mode, increase number of rounds
        if mode == "infinite":
            num_questions += 1


















