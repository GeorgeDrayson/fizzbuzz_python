class Fizzbuzz:

    def play(self, number):
        if self.divisible_by(15, number):
            return 'FizzBuzz'
        elif self.divisible_by(5, number):
            return 'Buzz'
        elif self.divisible_by(3, number):
            return 'Fizz'
        else:
            return number

    def divisible_by(self, divisor, number):
        return (number % divisor == 0)
