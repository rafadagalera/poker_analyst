## to do
# currently the draw cards function does not remove the cards from the deck, fix that you pos
# account for higher values when players have the same hand rank
# debug two pair function
## doing
# high card
## done
# full house
# straight flush
# straight 
# flush
# TOAK
# pair
# two pair
# 4OFK
# debug showdown
# return what the winning hand was

from cards import *

class Game:
    def __init__(self):
        self.player1_hand = []
        self.player2_hand = []
        self.community_cards = []
        self.cards = Cards()
        self.deck = self.cards.deck
        self.suits = self.cards.suits
        self.value_dict = self.cards.value_dict
        self.hand_ranks = self.cards.hand_ranks
        
    def preflop(self):
        self.cards.deal_card(self.player1_hand,2)
        self.cards.deal_card(self.player2_hand,2)
        print("Player 1 hand:",self.player1_hand,"Player 2 hand:",self.player2_hand)
        return self.player1_hand, self.player2_hand
    def flop(self):
        self.cards.deal_card(self.community_cards,3)
    def turn(self):
        self.cards.deal_card(self.community_cards,1)
    def river(self):
        self.cards.deal_card(self.community_cards,1)     
        
    # ordenação da mao completa do jogador por valores esta funcional 
    def get_full_player_hand(self,player_hand):
        full_player_hand = player_hand + self.community_cards
        return full_player_hand
    def split_cards(self,player_hand):
        values = [card[0] for card in player_hand]
        suits = [card[1] for card in player_hand]
        return values, suits
    def sort_player_hand(self, player_hand):
        values, suits = self.split_cards(player_hand)
        value_suit_pairs = [(value, suits[i]) for i, value in enumerate(values)]
        sorted_value_suit_pairs = sorted(value_suit_pairs, key=lambda x: value_dict[x[0]], reverse=True)
        sorted_hand = [value + suit for value, suit in sorted_value_suit_pairs]
        return sorted_hand
    def sort_player_hand_values(self, player_hand):
        values = [self.value_dict[card[0]] for card in player_hand]
        return sorted(values,reverse=True)
    
    # this section will determine the winner of the showdown
    def flush(self, player_hand):
        suits = [card[1] for card in player_hand]
        for i in range(4):
            if suits.count(suits[i]) == 5:
                return True        
    def straight(self, player_hand): 
        sorted_hand = self.sort_player_hand_values(player_hand)
        # checks if the last card is exactly one less in calue then current card
        def is_straight(hand):
            for i in range(4):
                if hand[i] + 1 != hand[i + 1]:
                    return False
            return True
        # checks each of the 3 possible 5-card hands
        for i in range(3):
            hand = sorted_hand[i:i+5]
            if is_straight(hand):
                return True
    def four_of_a_kind(self,player_hand):
        sorted_hand = self.sort_player_hand_values(player_hand)
        for i in range(4):
            if sorted_hand.count(sorted_hand[i]) == 4:
                return True
    def three_of_a_kind(self,player_hand):
        sorted_hand = self.sort_player_hand_values(player_hand)
        for i in range(4):
            if sorted_hand.count(sorted_hand[i]) == 3:
                return True
    def two_pair(self, player_hand):
        values = self.sort_player_hand_values(player_hand)
        pairs = [value for value in set(values) if values.count(value) == 2]
        return len(pairs) >= 2

    def pair(self, player_hand):
        values = self.sort_player_hand_values(player_hand)
        pairs = [value for value in set(values) if values.count(value) == 2]
        return len(pairs) >= 1
    
    def determine_hand_rank(self, player_hand):
        if self.straight(player_hand) and self.flush(player_hand):
            return 1
        elif self.four_of_a_kind(player_hand):
            return 2
        elif self.three_of_a_kind(player_hand) and self.pair(player_hand):
            return 3
        elif self.flush(player_hand):
            return 4
        elif self.straight(player_hand):
            return 5
        elif self.three_of_a_kind(player_hand):
            return 6
        elif self.two_pair(player_hand):
            return 7
        elif self.pair(player_hand):
            return 8
        else:
            return 9
    def tiebreaker(self,player1_hand,player2_hand):
        # if both players have the same hand rank, we need to determine the winner based on the
        # highest card in the hand. If the hands are still tied, we need to determine the
        # winner based on the second highest card in the hand, and so on.
        player1_hand_sorted = self.sort_player_hand(player1_hand)
        player2_hand_sorted = self.sort_player_hand(player2_hand)
        if self.determine_hand_rank(player1_hand) == 9:
            if player1_hand_sorted[0] > player2_hand_sorted[0]:
                print("Player 1 wins with High Card", player1_hand_sorted[0])
            elif player1_hand_sorted[0]< player2_hand_sorted[0]:
                print("Player 2 wins with High Card", player2_hand_sorted[0])
            else:
                if player1_hand_sorted[1] > player2_hand_sorted[1]:
                    print("Player 1 wins with High Card", player1_hand_sorted[1])
                elif player1_hand_sorted[1] < player1_hand_sorted[1]:
                    print("Player 2 wins with High Card", player2_hand_sorted[1])
                else:
                    return print("It's a tie! Split the pot")        
        # elif self.determine_hand_rank(hand) == 8:
                    
    # Determine the winner of the hand
    def showdown(self,player1_hand, player2_hand):
        player1_hand_rank = self.determine_hand_rank(player1_hand)
        player2_hand_rank = self.determine_hand_rank(player2_hand)
        
        if player1_hand_rank < player2_hand_rank:
            return print(f"Player 1 wins with {self.hand_ranks[player1_hand_rank]}")
        elif player1_hand_rank > player2_hand_rank:
            return print(f"Player 2 wins {self.hand_ranks[player2_hand_rank]}")
        else:
            return self.tiebreaker(player1_hand,player2_hand)
            
                
    def main(self):
        self.preflop()
        self.flop()
        # print("Flop: ",self.community_cards)
        self.turn()
        # print("Turn: ",self.community_cards)
        self.river()
        print("River: ",self.community_cards)
        player1_full_hand = self.get_full_player_hand(self.player1_hand)
        player2_full_hand = self.get_full_player_hand(self.player2_hand)
        # print(player1_full_hand,player2_full_hand)
        a = self.sort_player_hand(player1_full_hand)
        b = self.sort_player_hand(player2_full_hand)
        print(a,b)
        test = self.showdown(player1_full_hand,player2_full_hand)
        print(test)
        # print(self.sort_player_hand_values(player1_full_hand))
        # print(self.sort_player_hand_values(player2_full_hand))
        print(self.sort_player_hand(player1_full_hand))
        print(self.sort_player_hand(player2_full_hand))
        
game = Game()            
game.main()

        