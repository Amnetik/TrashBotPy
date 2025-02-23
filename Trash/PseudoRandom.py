import random

class NonRepeatingRandom:
    def __init__(self, n):
        self.n = n
        self.numbers = list(range(n + 1))  # List of numbers from 0 to n
        random.shuffle(self.numbers)  # Shuffle the list
        self.index = 0  # Start from the first element
    
    def get_next(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        else:
            # Optionally, reset or raise an error if you've exhausted the numbers
            # Reset the list and shuffle again if all numbers are used
            self.numbers = list(range(self.n + 1))
            random.shuffle(self.numbers)
            self.index = 0
            return self.get_next()