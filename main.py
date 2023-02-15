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

    elif user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard'):
        result = 1

    elif user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard'):
        result = 1

    elif user_choice == 'lizard' and (computer_choice == 'paper' or computer_choice == 'spock'):
        result = 1

    elif user_choice == 'paper' and (computer_choice == 'spock' or computer_choice == 'rock'):
        result = 1

    elif user_choice == 'spock' and (computer_choice == 'rock' or computer_choice == 'scissors'):
        result = 1

    else:
        result = 2

    show_winner(result)



