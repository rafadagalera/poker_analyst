from hands import *

class Game:
    def __init__(self):
        self.player1_hand = []
        self.player2_hand = []
        self.community_cards = []
        self.hands = Hands()
        self.deck = self.hands.load_deck()
        
    def preflop(self):
        self.deck, self.player1_hand = self.hands.draw_cards(self.deck, self.player1_hand, 2)
        self.deck, self.player2_hand = self.hands.draw_cards(self.deck, self.player2_hand, 2)
        print("Player 1 Hand:", self.player1_hand)
        print("Player 2 Hand:", self.player2_hand)
        # print("Remaining Deck:", self.deck)
    def flop(self):
        self.deck, self.community_cards = self.hands.draw_cards(self.deck, self.community_cards, 3)
        print("Flop:", self.community_cards)
    def turn(self):
        self.deck, self.community_cards = (self.hands.draw_cards(self.deck, self.community_cards, 1))
        print("Turn:", self.community_cards)
    def river(self):
        self.deck, self.community_cards = (self.hands.draw_cards(self.deck, self.community_cards,1))
        print("River:", self.community_cards)
    def main(self):
        self.preflop()
        self.flop()
        self.turn()
        self.river()

game = Game()
game.main()