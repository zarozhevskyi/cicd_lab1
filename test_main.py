import pytest
from main import generate_result, get_winner_message, get_sign_by_number
from constants import signs, messages


@pytest.mark.parametrize('user_choice, computer_choice, result', [(signs['ROCK'], signs['SCISSORS'], 1),
                                                                  (signs['ROCK'], signs['LIZARD'], 1),
                                                                  (signs['ROCK'], signs['PAPER'], 2),
                                                                  (signs['ROCK'], signs['SPOCK'], 2),
                                                                  (signs['PAPER'], signs['ROCK'], 1),
                                                                  (signs['PAPER'], signs['SCISSORS'], 2),
                                                                  (signs['PAPER'], signs['SPOCK'], 1),
                                                                  (signs['PAPER'], signs['LIZARD'], 2),
                                                                  (signs['SCISSORS'], signs['ROCK'], 2),
                                                                  (signs['SCISSORS'], signs['PAPER'], 1),
                                                                  (signs['SCISSORS'], signs['SPOCK'], 2),
                                                                  (signs['SCISSORS'], signs['LIZARD'], 1),
                                                                  (signs['LIZARD'], signs['ROCK'], 2),
                                                                  (signs['LIZARD'], signs['PAPER'], 1),
                                                                  (signs['LIZARD'], signs['SCISSORS'], 2),
                                                                  (signs['LIZARD'], signs['SPOCK'], 1),
                                                                  (signs['SPOCK'], signs['ROCK'], 1),
                                                                  (signs['SPOCK'], signs['PAPER'], 2),
                                                                  (signs['SPOCK'], signs['SCISSORS'], 1),
                                                                  (signs['SPOCK'], signs['LIZARD'], 2),
                                                                  (signs['ROCK'], signs['ROCK'], 0),
                                                                  (signs['PAPER'], signs['PAPER'], 0),
                                                                  (signs['SCISSORS'], signs['SCISSORS'], 0),
                                                                  (signs['LIZARD'], signs['LIZARD'], 0),
                                                                  (signs['SPOCK'], signs['SPOCK'], 0),
                                                                  ])
def test_generate_result(user_choice, computer_choice, result):
    assert generate_result(user_choice, computer_choice) == result


def test_winner_1_message():
    assert get_winner_message(1) == messages['WINNER_1']


def test_winner_2_message():
    assert get_winner_message(2) == messages['WINNER_2']


def test_tie_message():
    assert get_winner_message(0) == messages['TIE']


def test_invalid_winner_message():
    with pytest.raises(ValueError) as exception_info:
        get_winner_message(4)
    assert messages['INVALID_INPUT'] in str(exception_info)


def test_sign_rock():
    assert get_sign_by_number(1) == signs['ROCK']


def test_sign_paper():
    assert get_sign_by_number(2) == signs['PAPER']


def test_sign_scissors():
    assert get_sign_by_number(3) == signs['SCISSORS']


def test_sign_lizard():
    assert get_sign_by_number(4) == signs['LIZARD']


def test_sign_spock():
    assert get_sign_by_number(5) == signs['SPOCK']


def test_invalid_sign():
    with pytest.raises(ValueError) as exception_info:
        get_sign_by_number(6)
    assert messages['INVALID_INPUT'] in str(exception_info)
