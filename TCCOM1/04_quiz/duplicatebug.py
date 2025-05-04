import random


def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    print('''
    * Answer basic math questions *
    type <xxx> to end.
        ''')


def string_checker(question, valid_ans=("yes", "no")):
    # check if yes or no or not entering a valid answer
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:

            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()


def int_check_round(question):
    # checks if inter is higher/equal than 1 when entering amount of rounds
    while True:
        error = "enter an integer equal or more than 1."

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def int_check(question):
    # checks if answer is integer or not
    while True:
        error = "enter an integer. "

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
            # so that negative answers are correct
            if response < -100:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


print("Math quiz")
print()

want_instructions = yes_no("Do you want to see how the game is played? ")

if want_instructions == "yes":
    instructions()

mode = "regular"

rounds_played = 0

num_rounds = int_check_round("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n♾ Round {rounds_played + 1} (Infinite Mode) ♾"
    else:
        rounds_heading = f"\n💿 Round {rounds_played + 1} of {num_rounds} 💿"

    print(rounds_heading)

    right = 0 == "0"

    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    num3 = random.randint(0, 20)
    num4 = random.randint(0, 20)
    # random number between 0 - 10 ADD TOGETHER
    question1 = int_check(f"what is {num3} + {num2} = ")
    answer1 = num3 + num2
    if question1 == answer1:
        print(f"correct {right + 1} / 3")
        right += 1
    else:
        print(f"incorrect the answer was {answer1}")
        print(f"{right + 0} / 3")

    if mode == "infinite":
        rounds_heading = f"\n♾ Round {rounds_played + 1} (Infinite Mode) ♾"
    else:
        rounds_heading = f"\n💿 Round {rounds_played + 1} of {num_rounds} 💿"

    print(rounds_heading)

    question2 = int_check(f"what is {num4} - {num3} = ")
    answer2 = num4 - num3
    if question2 == answer2:
        print(f"correct {right + 1} / 3")
        right += 1
    else:
        print(f"incorrect the answer was {answer2}")
        print(f"{right + 0} / 3")

    if mode == "infinite":
        rounds_heading = f"\n♾ Round {rounds_played + 1} (Infinite Mode) ♾"
    else:
        rounds_heading = f"\n💿 Round {rounds_played + 1} of {num_rounds} 💿"

    print(rounds_heading)

    question3 = int_check(f"what is {num2} x {num1} = ")
    answer3 = num2 * num1
    if question3 == answer3:
        print(f"correct {right + 1} / 3")
        right += 1
    else:
        print(f"incorrect the answer was {answer3}")
        print(f"{right + 0} / 3")

    if mode == "infinite":
        rounds_heading = f"\n♾ Round {rounds_played + 1} (Infinite Mode) ♾"
    else:
        rounds_heading = f"\n💿 Round {rounds_played + 1} of {num_rounds} 💿"

    print(rounds_heading)

    rounds_played += 1

    if mode == "infinite":
        num_rounds += 1

if rounds_played > 0:
    print()
    print("thanks for playing")
