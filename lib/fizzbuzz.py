class Fizzbuzz:

    def play(self, number):
        if self.divisible_by_15(number):
            return 'FizzBuzz'
        elif self.divisible_by_5(number):
            return 'Buzz'
        elif self.divisible_by_3(number):
            return 'Fizz'
        else:
            return number

    def divisible_by_15(self, number):
        return self.divisible_by(15, number)

    def divisible_by_5(self, number):
        return self.divisible_by(5, number)

    def divisible_by_3(self, number):
        return self.divisible_by(3, number)

    def divisible_by(self, divisor, number):
        return (number % divisor == 0)
