import random


# the instructions
def instructions():
    """prints instructions"""
    print('''
        Push <enter> for Normal mode 5 rounds
         Otherwise type how many numbers for Custom 
          rounds
           Each round gives 4 questions for
            addition,
             subtraction, multiplication and division.
              if u dont give an answer its wrong
        ''')


def string_checker(question, valid_ans=("yes", "no")):
    """checks if the user enters yes or no"""
    # check if yes or no or not entering a valid answer
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for thing in valid_ans:

            if thing == user_response:
                return thing

            elif user_response == thing[0]:
                return thing

        print(error)
        print()


def int_check(question):
    """checks if the user enters a number"""
    # checks if answer is integer or not
    while True:
        error = "enter an integer or a number equal to/greater than 1. "

        to_check = input(question)

        if to_check == "":
            # if person press enters it returns regular which used for when asking which mode
            return "Regular"

        try:
            response = int(to_check)
            # when entering number of rounds if its below 1 it will be invalid
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


print()
print("✖️➕Math Quiz➖➗")
print()

want_instructions = string_checker("Do you want to see instructions? ")

if want_instructions == "yes":
    # if user types yes/y it shows the instructions
    instructions()

mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""
game_history = []
all_scores = []

num_rounds = int_check("How many rounds would you like? Push <enter> for 5 rounds: ")
# IF user press enter it does normal 5 rounds if it enters a number that is the amount of rounds

if num_rounds == "Regular":
    mode = "Regular"
    num_rounds = 5
    # regular mode has 5 round

while rounds_played < num_rounds:

    if mode == "Regular":
        rounds_heading = f"\n➰ Round {rounds_played + 1} of {num_rounds} ➰"
    else:
        rounds_heading = f"\n➿ Custom Round {rounds_played + 1} of {num_rounds} ➿"
    # the user picks a game of 5 rounds or can type as many rounds as they want

    print(rounds_heading)

    right = 0
    # it shows the 0 / 4 when counting how much answers you got right per round

    num1 = random.randint(1, 12)
    num11 = random.randint(0, 20)
    num2 = random.randint(1, 12)
    num22 = random.randint(0, 20)
    num3 = random.randint(0, 20)
    num4 = random.randint(20, 30)

    # generates random number between 0 - 20 for each math question
    question1 = int_check(f"❔What is {num11} ➕ {num22} = ")
    # adds 2 random numbers between 0 - 20
    answer1 = num11 + num22
    if question1 == answer1:
        print(f"✔️correct")
        right += 1
        # means that the user got one question right and adds up with the other questions
    else:
        print(f"✖️incorrect the answer was {answer1}")
        print(f"{right + 0} / 4")

    question2 = int_check(f"❔What is {num4} ➖ {num3} = ")
    # subtracts 2 random numbers between 0 - 20
    answer2 = num4 - num3
    if question2 == answer2:
        print(f"✔️correct")
        right += 1
    else:
        print(f"✖️incorrect the answer was {answer2}")
        print(f"{right + 0} / 4")

    question3 = int_check(f"❔What is {num2} ✖️ {num1}? = ")
    answer3 = num2 * num1
    if question3 == answer3:
        print(f"✔️correct")
        right += 1
    else:
        print(f"✖️incorrect the answer was {answer3}")
        print(f"{right + 0} / 4")

    num5 = random.randint(1, 12)
    num6 = random.randint(1, 12)
    # generates random number 1 - 12 for division

    question4 = int_check(f"❔What is {num6 * num5} ➗ {num6}? = ")
    # multiplies 2 random numbers between 0 - 12 (num6 * num5) and divided by the divisor (num6)
    answer4 = num6 * num5 / num6
    # if answer is correct = correct
    if question4 == answer4:
        print(f"✔️correct")
        right += 1
    else:
        print(f"✖️incorrect the answer was {answer4}")
        print(f"{right + 0} / 4")

    rounds_played += 1

    history_feedback = f"Round {rounds_played}: {right} / 4 | {right * 25}%"
    # shows percentage rate of what the user got right for every round
    game_history.append(history_feedback)

    all_scores.append(right)

if rounds_played > 0:

    see_history = string_checker("\nDo you want to see your game history?📃 ")
    # shows game history if it says yes
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing. ")
