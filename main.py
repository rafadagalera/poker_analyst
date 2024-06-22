import random, json

class Hands:
    def __init__(self):
        self.player1_hand = []
        self.player2_hand = []
        self.cards = []
    def draw_cards(self):
        # This will pick a random hand from the file of possible hands and assure that every player has a unique hand
        try:
            with open('possible_hands.json', 'r') as f:
                possible_hands = json.load(f)
                hand1 = random.choice(possible_hands)
                hand2 = random.choice(possible_hands)

                # This redraws the second hand if the two players have the same hand
                if hand1 == hand2:
                    hand2 = random.choice(possible_hands)
    
                self.player1_hand = hand1
                self.player2_hand = hand2
                print(self.player1_hand, self.player2_hand)
        except FileNotFoundError:
            print("File not found. Please make sure 'possible_hands.json' is in the same directory")

        pass
    def evaluate_cards(self):
        # This will determine which hand is stronger
        pass

hands = Hands()
hands.draw_cards()