import random


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


division1 = random.randint = ["4 / 2"]

question1 = int_check(f"What is {division1} / {division2} = ")
answer1 = random.randint == division1 / division2
if question1 == answer1:
    print("correct")
else:
    print("incorrect")
