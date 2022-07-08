from random import choice

class Game:
    def __init__(self, player):
        self.player = player
        self.computer = self.choose()

    def choose(self):
        list = ['rock', 'paper', 'scissors']
        return choice(list)

    def compare(self):
        if self.player == self.computer:
            return 'draw'
        elif self.player == 'rock' and self.computer == 'scissors':
            return 'win'
        elif self.player == 'scissors' and self.computer == 'paper':
            return 'win'
        elif self.player == 'paper' and self.computer == 'rock':
            return 'win'
        else:
            return 'loss'