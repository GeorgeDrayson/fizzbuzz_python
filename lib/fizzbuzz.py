class Fizzbuzz(object):

    def play(self, number):
        if self.is_divisible_by_15(number):
            return 'FizzBuzz'
        elif self.is_divisible_by_5(number):
            return 'Buzz'
        elif self.is_divisible_by_3(number):
            return 'Fizz'
        else:
            return number

    def is_divisible_by_15(self, number):
        return self.is_divisible_by(15, number)

    def is_divisible_by_5(self, number):
        return self.is_divisible_by(5, number)

    def is_divisible_by_3(self, number):
        return self.is_divisible_by(3, number)

    def is_divisible_by(self, divisor, number):
        return (number % divisor == 0)

    def one_to_hundred(self):
        list = []
        for i in range(1,101):
            list.append(self.play(i))
        return ', '.join(str(x) for x in list)
