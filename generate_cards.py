import json

class Cards:
    def __init__(self):
        self.suits = ["S", "C", "D", "H"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        self.possible_cards = []

    def generate_possible_cards(self):
        for suit in self.suits:
            for value in self.values:
                self.possible_cards.append(value + suit)
                
        self.export_possible_cards()        
        return

    def export_possible_cards(self):
        with open('possible_cards.json', 'w') as f:
            json.dump(self.possible_cards, f, indent= 4)

cards = Cards()
cards.generate_possible_cards()