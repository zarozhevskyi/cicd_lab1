import random
import constants


def draw_line():
    print('===========================================')


def show_winner(result):
    if result == 0:
        print("Tie! Try your luck next time.")
    elif result == 1:
        print("Congratulations. You won!")
    elif result == 2:
        print("Sorry, you lost. Good luck next time!")


def generate_result(user_choice, computer_choice):
    result = None

    if user_choice == computer_choice:
        result = 0

    elif user_choice == constants.ROCK and (computer_choice == constants.SCISSORS or computer_choice == constants.LIZARD):
        result = 1

    elif user_choice == constants.SCISSORS and (computer_choice == constants.PAPER or computer_choice == constants.LIZARD):
        result = 1

    elif user_choice == constants.LIZARD and (computer_choice == constants.PAPER or computer_choice == constants.SPOCK):
        result = 1

    elif user_choice == constants.PAPER and (computer_choice == constants.SPOCK or computer_choice == constants.ROCK):
        result = 1

    elif user_choice == constants.SPOCK and (computer_choice == constants.ROCK or computer_choice == constants.SCISSORS):
        result = 1

    else:
        result = 2

    show_winner(result)


def get_sign_by_number(number):
    if number == 1:
        return constants.ROCK
    if number == 2:
        return constants.PAPER
    if number == 3:
        return constants.SCISSORS
    if number == 4:
        return constants.LIZARD
    return constants.SPOCK


def get_random_sign():
    number = random.randint(1, 5)
    return get_sign_by_number(number)


def show_choices(user_choice, computer_choice):
    print(f'User choice: {user_choice}')
    print(f'Computer choice: {computer_choice}')


def main():
    draw_line()
    print('ROCK PAPER SCISSORS LIZARD SPOCK')
    draw_line()
    print('Options')
    draw_line()
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    print('4. Lizard')
    print('5. Spock')
    draw_line()
    enter_condition = True
    while enter_condition:
        print('Enter your choice:')
        try:
            user_input = int(input())
            if user_input == 1 or user_input == 2 or user_input == 3 or user_input == 4 or user_input == 5:
                enter_condition = False
            else:
                print('A number must be equal to 1, 2, 3, 4 or 5')
        except:
            print('Please enter a number!')
        draw_line()
    user_choice = get_sign_by_number(user_input)
    computer_choice = get_random_sign()
    show_choices(user_choice, computer_choice)
    draw_line()
    generate_result(user_choice, computer_choice)


main()
