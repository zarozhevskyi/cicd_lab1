def draw_line():
    print('===========================================')


def show_user_victory_message():
    print("Congratulations. You won!")


def show_computer_victory_message():
    print("Sorry, you lost. Good luck next time!")


def show_tie_message():
    print("Tie! Try your luck next time.")


def generate_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        show_tie_message()

    elif user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard'):
        show_user_victory_message()

    elif user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard'):
        show_user_victory_message()

    elif user_choice == 'lizard' and (computer_choice == 'paper' or computer_choice == 'spock'):
        show_user_victory_message()

    elif user_choice == 'paper' and (computer_choice == 'spock' or computer_choice == 'rock'):
        show_user_victory_message()

    elif user_choice == 'spock' and (computer_choice == 'rock' or computer_choice == 'scissors'):
        show_user_victory_message()

    else:
        show_computer_victory_message()


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


main()
