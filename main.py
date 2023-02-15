def drawLine():
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
    drawLine()
    print('ROCK PAPER SCISSORS LIZARD SPOCK')
    drawLine()
    print('Options')
    drawLine()
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    print('4. Lizard')
    print('5. Spock')
    drawLine()


main()