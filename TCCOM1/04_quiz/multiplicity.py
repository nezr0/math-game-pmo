import random


def int_check(question):
    while True:
        error = "enter an integer."

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


num1 = random.randint(0, 12)
num2 = random.randint(0, 12)

quest = int_check(f"what is {num1} x {num2} = ")
answer = num1 * num2

if quest == answer:
    print()
    print("correct")
else:
    print()
    print(f"incorrect the answer was {answer}")
