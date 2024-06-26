from generate_cards import deck, value_dict, suits, hand_ranks
import random

class Cards:
    def __init__(self, deck=deck, value_dict=value_dict, hand_ranks = hand_ranks):
        self.deck = deck
        self.value_dict = value_dict
        self.suits = suits
        self.discard_pile = []
        self.hand_ranks = hand_ranks
    def deal_card(self,destination,amount):
        for i in range(amount):
            card = random.choice(self.deck)
            destination.append(card)
            self.deck.remove(card)
    def burn_card(self,amount):
        for i in range(amount):
            self.discard_pile.append(random.choice(self.deck))
            return self.deck
    def get_card_value(self,card):
        return self.value_dict[card]
            
cards = Cards()

# print(cards.get_card_value("A"))    