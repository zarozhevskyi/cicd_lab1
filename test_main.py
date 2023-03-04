import pytest
from main import generate_result, get_winner_message, get_sign_by_number
from constants import signs, messages


def test_rock_vs_scissors():
    assert generate_result(signs['ROCK'], signs['SCISSORS']) == 1


def test_rock_vs_lizard():
    assert generate_result(signs['ROCK'], signs['LIZARD']) == 1


def test_rock_vs_paper():
    assert generate_result(signs['ROCK'], signs['PAPER']) == 2


def test_rock_vs_spock():
    assert generate_result(signs['ROCK'], signs['SPOCK']) == 2


def test_paper_vs_rock():
    assert generate_result(signs['PAPER'], signs['ROCK']) == 2


def test_paper_vs_scissors():
    assert generate_result(signs['PAPER'], signs['SCISSORS']) == 1


def test_paper_vs_spock():
    assert generate_result(signs['PAPER'], signs['SPOCK']) == 1


def test_paper_vs_lizard():
    assert generate_result(signs['PAPER'], signs['LIZARD']) == 2


def test_scissors_vs_rock():
    assert generate_result(signs['SCISSORS'], signs['ROCK']) == 2


def test_scissors_vs_paper():
    assert generate_result(signs['SCISSORS'], signs['PAPER']) == 1


def test_scissors_vs_spock():
    assert generate_result(signs['SCISSORS'], signs['SPOCK']) == 2


def test_scissors_vs_lizard():
    assert generate_result(signs['SCISSORS'], signs['LIZARD']) == 1


def test_lizard_vs_rock():
    assert generate_result(signs['LIZARD'], signs['ROCK']) == 2


def test_lizard_vs_paper():
    assert generate_result(signs['LIZARD'], signs['PAPER']) == 1


def test_lizard_vs_scissors():
    assert generate_result(signs['LIZARD'], signs['SCISSORS']) == 2


def test_lizard_vs_spock():
    assert generate_result(signs['LIZARD'], signs['SPOCK']) == 1


def test_spock_vs_rock():
    assert generate_result(signs['SPOCK'], signs['ROCK']) == 1


def test_spock_vs_paper():
    assert generate_result(signs['SPOCK'], signs['PAPER']) == 2


def test_spock_vs_scissors():
    assert generate_result(signs['SPOCK'], signs['SCISSORS']) == 1


def test_spock_vs_lizard():
    assert generate_result(signs['SPOCK'], signs['LIZARD']) == 1


def test_rock_vs_rock():
    assert generate_result(signs['ROCK'], signs['ROCK']) == 0


def test_paper_vs_paper():
    assert generate_result(signs['PAPER'], signs['PAPER']) == 0


def test_scissors_vs_scissors():
    assert generate_result(signs['SCISSORS'], signs['SCISSORS']) == 0


def test_lizard_vs_lizard():
    assert generate_result(signs['LIZARD'], signs['LIZARD']) == 0


def test_spock_vs_spock():
    assert generate_result(signs['SPOCK'], signs['SPOCK']) == 0


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
