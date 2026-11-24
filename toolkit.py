# Week 8 Final Project - Personal Mini-Toolkit

import random


# TOOL 1: Number Guessing Game
# The user tries to guess a random number between 1 and 10.

def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I have chosen a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if guess < 1 or guess > 10:
            print("Please choose a number between 1 and 10.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break


# TOOL 2: To-Do List
# Users can add, view, and remove their tasks.

def todo_list():
    tasks = []

    while True:
        print("\n--- My To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task removed: {removed}")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 4.")


# TOOL 3: Simple Calculator
# The user can perform four basic mathematical operations.

def calculator():
    print("\n--- Simple Calculator ---")

    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

    except ValueError:
        print("Please enter valid numbers.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Choose an operation (1-4): ")

    if operation == "1":
        result = number1 + number2

    elif operation == "2":
        result = number1 - number2

    elif operation == "3":
        result = number1 * number2

    elif operation == "4":
        if number2 == 0:
            print("Cannot divide by zero.")
            return

        result = number1 / number2

    else:
        print("Invalid operation.")
        return

    print(f"Result: {result}")


# MAIN PROGRAM
# This menu continues until the user chooses Quit.

def main():
    print("Welcome to your Personal Mini-Toolkit!")
    print("Choose a tool and enjoy using it.")

    while True:
        print("\n========== PERSONAL MINI-TOOLKIT ==========")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            calculator()

        elif choice == "4":
            print("Thank you for using my Personal Mini-Toolkit!")
            print("Goodbye. Have a great day!")
            break

        else:
            print("Sorry, that is not a valid choice. Please try again.")


# Start the program.
if __name__ == "__main__":
    main()
