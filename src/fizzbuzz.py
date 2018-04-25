class Fizzbuzz(object):

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
        return (number % 15 == 0)

    def divisible_by_5(self, number):
        return (number % 5 == 0)

    def divisible_by_3(self, number):
        return (number % 3 == 0)
