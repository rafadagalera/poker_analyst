from game import *

class Player:
    def __init__(self,uid):
        self.id = uid
        self.game = Game()
        self.hand = game.player1_hand
        self.folded = False
    def check(self):
        pass
    def bet(self,amount):
        pass
    def call(self,amount):
        pass
    def raise_bet(self,amount):
        pass
    def fold(self):
        pass
    