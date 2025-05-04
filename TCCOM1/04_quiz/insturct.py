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
    * Answer math question *
        ''')


print("Math quest")
print()

want_instructions = yes_no("Do you want to see how the game is played?")

if want_instructions == "yes":
    instructions()








