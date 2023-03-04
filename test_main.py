import pytest
from main import generate_result
from constants import signs


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