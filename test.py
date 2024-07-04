from cards import *

     
class Player():
    def __init__(self,stack):
        self.stack = stack
        self.hand = []
        self.bet_amount = 0
        self.has_folded = False
        self.is_button = False
    def bet(self,amount):
        if self.stack >= amount:
            self.bet_amount += amount
            self.stack -= amount
        else:
            print("You don't have enough money to bet that much")
        return amount
    def call(self,amount):
        self.bet(amount)
        return amount
    def raise_bet(self,amount):
        self.bet(amount)    
        return amount
    def fold(self):
        self.has_folded = True
    def check(self):
        pass
    
test_player1 = Player(3000)
test_player2 = Player(3000)    

class Game(Player):
    def __init__(self,player1,player2):
        self.cards = Cards()
        self.pot = 0
        self.player1 = player1
        self.player2 = player2
    def shuffle_button(self):
        if self.player1.is_button == True:
            self.player1.is_button = False
            self.player2.is_button = True
        else:
            self.player1.is_button = True
            self.player2.is_button = False
        
    def game_turn(self):
        while True:            
            player_action = int(input("What would you like to do? \n1 - Check \n2 - Bet \n3 - Fold \n"))
            if player_action == 1:
                self.player1.check()
                break
            elif player_action == 2:
                bet_amount = int(input("How much would you like to bet? \n"))
                self.player1.bet(bet_amount)
                self.player1.bet_amount += bet_amount
                break
            elif player_action == 3:
                self.player1.fold()
                break
            else:
                print("Invalid input")
        
    def preflop(self):
        self.cards.deal_card(self.player1.hand,2)
        self.cards.deal_card(self.player2.hand,2)
        print(f"Player 1 hand: {self.player1.hand} Player 2 hand: {self.player2.hand}")
    def reset(self):
        self.cards = Cards()
        self.pot = 0
        self.player1.hand.clear()
        self.player2.hand.clear()
    def main(self):
        while True:
            self.preflop()
            self.game_turn()
            self.shuffle_button()
            play_again = str(input("Would you like to play again? Type N to quit")).upper()
            if play_again == "N":
                break
            self.reset()
            
            

game_test = Game(test_player1,test_player2)
game_test.main()        
print(game_test.player1.is_button)
print(game_test.player2.is_button)

        
        