"""Defines Player and Dealer classes"""

# Init Player
class Player():

    def __init__(self, balance=100, wager = 0):
        self.balance = balance
        self.wager = wager
        self.card = []

    def score(self):

        aces = 0
        total = 0

        # Get the score of all cards except aces
        for c in self.card:
            c = c % 100
            if c in range(2,11):
                total += c
            if c > 10:
                total += 10
            # Increment the number of aces
            if c == 1:
                aces += 1

        # Use the best number for the aces to prevent a bust
        for i in range(0, aces):
            if aces * 11 + total > 21:
                total += 1
                aces -= 1
            else:
                total += 11
                aces -= 1

        # Return the total score
        return total


# init Dealer
class Dealer():
    def __init__(self):
        self.card = []
        self.initial = True

    def score(self):

        aces = 0
        total = 0

        # Get the score of all cards except aces
        for c in self.card:
            c = c % 100
            if c in range(2,11):
                total += c
            if c > 10:
                total += 10
            # Increment the number of aces
            if c == 1:
                aces += 1

        # Use the best number for the aces to prevent a bust
        for i in range(0, aces):
            if aces * 11 + total > 21:
                total += 1
                aces -= 1
            else:
                total += 11
                aces -= 1

        # Return the total score
        return total
