import random, json

# The first version of this game only allows for two players and discredits bets and fold


class Hands:
    def __init__(self):
        self.player1_hand = []
        self.player2_hand = []
        self.hand_types = ("Royal Flush","Straight Flush","Four-of-a-Kind","Full House","Flush","Straight","Three-of-a-Kind","Two Pair","One Pair","High Card")
        self.cards = []


    def draw_cards(self):
        ### Please update this function to draw a single card each time, remove that card from the deck and keep track of every hand on another function-+
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

class Game:
    def __init__(self):
        self.community_cards = 0
        self.hands = Hands()
        self.hands.draw_cards()
    def preflop(self):
        # This will handle the preflop events
        print("My hand:",self.hands.player1_hand)
        # Here only for testing purposes, will remove later
        print("Opponent's hand:", self.hands.player2_hand)
        pass
    def flop(self):
        #This will handle the flop events
        if self.community_cards == 0:
            first_community_card = random.choice(possible_hands)
        pass
    def turn(self):
        #This will handle the turn events
        pass
    def river(self):
        #This will handle the river events
        pass
    def determine_winner():
        #This will determine the winner of the hand
        pass

    def main(self):
        self.preflop()
        self.flop()
        self.turn()
        self.river()
        self.determine_winner()



