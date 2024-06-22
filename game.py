from hands import *

class Game:
    def __init__(self):
        self.player1_hand = []
        self.player2_hand = []
        self.player1_stack = 0
        self.player2_stack = 0
        self.pot = 0
        self.community_cards = []
        self.hands = Hands()
        self.deck = self.hands.load_deck()
        self.values = {'T': 10, "J":11, "Q":12, "K":13, "A":14}
        # self.flush = False
        # self.straight = False
        # self.quads = False
        # self.triplets = False
        # self.pair = False
        
        
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
    def determine_hand_rank(self,hand):
        # Rank these hands in order:
        # 9: Royal Flush
        # 8: Straight Flush
        # 7: Four of a Kind
        # 6: Full House
        # 5: Flush
        # 4: Straight
        # 3: Three of a Kind
        # 2: Two Pair
        # 1: One Pair
        # 0: High Card
        
        hand_strength = 0
        full_player_hand = [hand + self.community_cards]
        sorted_hand = []
        for card in full_player_hand:
            value = card[:-1]
            suit = card[-1]
            sorted_hand.append((value,suit))
        print(sorted_hand)
            
    def determine_winner(self,hand1,hand2):
        hand1_rank = self.determine_hand_rank(hand1)
        hand2_rank = self.determine_hand_rank(hand2)
        
    def main(self):
        self.preflop()
        self.flop()
        self.turn()
        self.river()
        self.determine_winner(self.player1_hand, self.player2_hand)

game = Game()
game.main()