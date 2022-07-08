from flask import flash

class Player:

    def __init__(self, name):
        self.player = name
        self.credit = 0

    def add(self):
        self.credit +=10

    def pay(self):
        self.credit -= 3


    def win(self):
        self.credit +=4