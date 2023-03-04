import pytest
from main import generate_result
from constants import signs


def test_rock_vs_scissors():
    assert generate_result(signs['ROCK'], signs['SCISSORS']) == 1
