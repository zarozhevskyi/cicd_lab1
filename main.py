import random
from constants import signs, messages


def draw_line():
    print('===========================================')


def get_winner_message(result):
    if result == 0:
        return messages['TIE']
    elif result == 1:
        return messages['WINNER_1']
    elif result == 2:
        return messages['WINNER_2']
    raise ValueError(messages['INVALID_INPUT'])


def generate_result(user_choice, computer_choice):
    result = None

    if user_choice == computer_choice:
        result = 0

    elif (user_choice == signs['ROCK'] and
          computer_choice in (signs['SCISSORS'], signs['LIZARD'])):
        result = 1

    elif (user_choice == signs['SCISSORS'] and
          computer_choice in (signs['PAPER'], signs['LIZARD'])):
        result = 1

    elif (user_choice == signs['LIZARD'] and
          computer_choice in (signs['PAPER'], signs['SPOCK'])):
        result = 1

    elif (user_choice == signs['PAPER'] and
          computer_choice in (signs['SPOCK'], signs['ROCK'])):
        result = 1

    elif (user_choice == signs['SPOCK'] and
          computer_choice in (signs['ROCK'], signs['SCISSORS'])):
        result = 1

    else:
        result = 2

    return result


def get_sign_by_number(number):
    if number == 1:
        return signs['ROCK']
    if number == 2:
        return signs['PAPER']
    if number == 3:
        return signs['SCISSORS']
    if number == 4:
        return signs['LIZARD']
    if number == 5:
        return signs['SPOCK']
    raise ValueError(messages['INVALID_INPUT'])


def get_random_sign(start=1, end=5):
    number = random.randint(start, end)
    return get_sign_by_number(number)


def show_choices(user_choice, computer_choice):
    print(f'User choice: {user_choice}')
    print(f'Computer choice: {computer_choice}')


def main():
    while True:
        print()
        print()
        draw_line()
        print('ROCK PAPER SCISSORS LIZARD SPOCK')
        draw_line()
        print('Options')
        draw_line()
        print('1. Rock', '2. Paper', '3. Scissors', '4. Lizard', '5. Spock',
              '6. Exit', sep='\n')
        draw_line()
        while True:
            try:
                user_input = int(input('Enter your choice: '))
                if user_input in (1, 2, 3, 4, 5):
                    draw_line()
                    break
                elif user_input == 6:
                    return
                else:
                    print('A number must be equal to 1, 2, 3, 4, 5 or 6')
            except Exception:
                print('Please enter a number!')
            draw_line()
        user_choice = get_sign_by_number(user_input)
        computer_choice = get_random_sign()
        show_choices(user_choice, computer_choice)
        draw_line()
        result = generate_result(user_choice, computer_choice)
        print(get_winner_message(result))


if __name__ == '__main__':
    main()
