import pytest
from fizzbuzz import Fizzbuzz

def describe_multiples_of_3():

    def test_returns_fizz_with_3():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.play(3) == 'Fizz'

    def test_returns_fizz_with_6():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.play(6) == 'Fizz'

def describe_multiples_of_5():

    def test_returns_buzz_with_5():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.play(5) == 'Buzz'

    def test_returns_buzz_with_10():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.play(10) == 'Buzz'

def describe_multiples_of_15():

    def test_returns_fizzbuzz_with_15():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.play(15) == 'FizzBuzz'

    def test_returns_fizzbuzz_with_30():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.play(30) == 'FizzBuzz'

def describe_normal_numbers():

    def test_returns_4_with_4():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.play(4) == 4

    def test_returns_7_with_7():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.play(7) == 7
