import pytest
from fizzbuzz import Fizzbuzz

def test_returns_fizz_with_3():
    fizzbuzz = Fizzbuzz()
    assert fizzbuzz.play(3) == 'Fizz'
