import random

init = input("Wanna throw the dice? (y/n):")


if init == "y":
    result = random.randint(1, 6)
    print("You rolled a", result)
    again = input("Wanna throw again? (y/n): ")
    while again == "y":
        result = random.randint(1, 6)
        print("You rolled a", result)
        again = input("Wanna throw again? (y/n): ")
        if again == "n":
            print("Goodbye!")
            exit
elif init == "n":
        print("Goodbye!")
        exit