import sys
sys.path.insert(0, '/Users/georgedrayson/Projects/fizzbuzz_python/lib')

from fizzbuzz import Fizzbuzz

def describe_is_divisible_by():

    def test_returns_true():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.is_divisible_by(3,3) == True

    def test_returns_false():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.is_divisible_by(3,4) == False

def describe_is_divisible_by_15():

    def test_returns_true():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.is_divisible_by_15(30) == True

    def test_returns_false():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.is_divisible_by_15(4) == False

def describe_is_divisible_by_5():

    def test_returns_true():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.is_divisible_by_5(5) == True

    def test_returns_false():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.is_divisible_by_5(4) == False

def describe_is_divisible_by_3():

    def test_returns_true():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.is_divisible_by_3(3) == True

    def test_returns_false():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.is_divisible_by_3(4) == False

def describe_play():

    def describe_multiples_of_3():

        def test_returns_fizz_with_3():
            fizzbuzz = Fizzbuzz()
            assert fizzbuzz.play(3) == 'Fizz'

    def describe_multiples_of_5():

        def test_returns_buzz_with_5():
            fizzbuzz = Fizzbuzz()
            assert fizzbuzz.play(5) == 'Buzz'

    def describe_multiples_of_15():

        def test_returns_fizzbuzz_with_15():
            fizzbuzz = Fizzbuzz()
            assert fizzbuzz.play(15) == 'FizzBuzz'

    def describe_normal_numbers():

        def test_returns_4_with_4():
            fizzbuzz = Fizzbuzz()
            assert fizzbuzz.play(4) == 4

def describe_one_to_100():

    def test_returns_1_to_100():
        fizzbuzz = Fizzbuzz()
        assert fizzbuzz.one_to_hundred() == '1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, 41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz, 61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, FizzBuzz, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, FizzBuzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz'
