import json

class Possible_Hands:
    def __init__(self):
        self.suits = ["S", "C", "D", "H"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        self.possible_hands = self.generate_possible_hands()

    def generate_possible_hands(self):
        possible_hands_set = set()  # Use a set to avoid duplicates
        possible_hands_list = []

        for suit in self.suits:
            for value in self.values:
                first_card = value + suit
                for suit2 in self.suits:
                    for value2 in self.values:
                        second_card = value2 + suit2
                        if first_card != second_card:  # Ensure the two cards are different
                            # Sort the cards within each pair
                            sorted_hand = sorted([first_card, second_card])
                            sorted_hand_tuple = tuple(sorted_hand)  # Convert to tuple for set

                            if sorted_hand_tuple not in possible_hands_set:
                                possible_hands_set.add(sorted_hand_tuple)
                                possible_hands_list.append(sorted_hand)

        self.export_possible_hands(possible_hands_list)
        return possible_hands_list

    def export_possible_hands(self, possible_hands_list):
        with open('possible_hands.json', 'w') as f:
            json.dump(possible_hands_list, f, indent=4)

hands = Possible_Hands()

