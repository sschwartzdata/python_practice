import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


# Define Card class
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# Defining deck class
class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Creating the card object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def __str__(self):
        deck_comp = ''  
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Deal a card
    def deal_one(self):
        return self.all_cards.pop()

# Defining Player Class
class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0
        self.aces = 0

    def add_cards(self, new_card):
        # If single card
        self.hand.append(new_card)
        self.value += values[new_card.rank]
        if new_card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        card_hand = ''
        player_name = self.name.__str__()
        for card in self.hand:
            card_hand += card.__str__() + '\n'
        return player_name + "'s hand: \n" + card_hand


# Defining betting chips
class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def __str__(self):
        total = ''
        total = self.total.__str__()
        return total


# Function for betting chips
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def deal(deck):
    deal_card = deck.deal_one()
    return deal_card


# A function that checks to see if the hand is bust
def bust_check(player):
    if player.value > 21:
        return True
    else:
        return False


def black_jack_test(player_hand):
    if ((player_hand[0].rank in ['Ten', 'Jack', 'Queen', 'King'])
            and (player_hand[1].rank in ['Ace'] is True)):
        return True
    elif ((player_hand[1].rank in ['Ten', 'Jack', 'Queen', 'King'])
          and (player_hand[0].rank in ['Ace']) is True):
        return True
    else:
        return False


def black_jack_test_dealer(dealer_hand):
    if ((dealer_hand[0].rank in ['Ten', 'Jack', 'Queen', 'King'])
            and (dealer_hand[1].rank in ['Ace'] is True)):
        return True
    elif ((dealer_hand[1].rank in ['Ten', 'Jack', 'Queen', 'King'])
            and (dealer_hand[0].rank in ['Ace']) is True):
        return True
    else:
        return False


# A function to test who won
def win_check(dealer, player):
    if dealer.value > player.value:
        print('The dealer has won. Better luck next time')
        chips.lose_bet()
    elif dealer.value == player.value:
        print('It is a draw! No one wins.')
    else:
        print('You have won! Congratulations!')
        chips.win_bet


# Black Jack Game

def black_jack(chips, name, player):
    dealer = Player('Dealer')
    new_deck = Deck()
    new_deck.shuffle()
    game_on = True

    # Taking bet
    print(f'The total ammount that you can bet is : {chips}')
    bet = take_bet(chips)

    # Deal cards to player
    deal_card_first = deal(new_deck)
    player.add_cards(deal_card_first)
    player.adjust_for_ace()
    print(f'Your first card is {deal_card_first}.')
    deal_card_second = deal(new_deck)
    player.add_cards(deal_card_second)
    player.adjust_for_ace()
    print(f'Your first card is {deal_card_second}.')

    dealer_first = deal(new_deck)
    dealer.add_cards(dealer_first)
    dealer.adjust_for_ace()
    print(f'The dealer reveals their first card as {dealer_first}')
    dealer_second = deal(new_deck)
    dealer.add_cards(dealer_second)
    dealer.adjust_for_ace()
    print('The dealer places their second card face down')

    # checking for BJ
    if black_jack_test_dealer(dealer.hand) is True:
        print('The dealer shows their hand.')
        print(f'The dealer places {dealer} on the table.')
        print('Sorry, the dealer won this game. Better luck next time.')
        chips.lose_bet()

    if black_jack_test(player.hand) is True:
        print(player)
        print('That is Black Jack! You won!')
        chips.win_bet()

    else:
        pass

        while game_on is True:
            # Ask for hit
            hit = input(f'{player.name}, would you like another card? (Y/N)')
            if hit.upper() == 'Y':
                deal_card = deal(new_deck)
                player.add_cards(deal_card)
                player.adjust_for_ace()
                print(f'Your new card is {deal_card}.')
                print(player)
                bust = bust_check(player)
                if bust is True:
                    print('Bust! You lost this game. Better luck next time!')
                    chips.lose_bet()
                    return 0

            if hit.upper() == 'N':
                # Dealer's turn
                while dealer.value < 17:
                    deal_card = deal(new_deck)
                    dealer.add_cards(deal_card)
                    dealer.adjust_for_ace()
                    bust = bust_check(dealer)
                    if bust is True:
                        print('The dealer reveals their hand.')
                        print(dealer)
                        print('The dealer is bust! You won!')
                        chips.win_bet()
                        return 0


                print('The dealer reveals their hand.')
                print(dealer)
                if dealer.value > player.value:
                    print('The dealer has won. Better luck next time')
                    chips.lose_bet()
                elif dealer.value > player.value:
                    print('It is a draw! No one wins.')
                else:
                    print('You have won! Congratulations!')
                    chips.win_bet()
                return 0


def main():
    name = input("Welcome! What is your name?")
    player = Player(name)
    chips = Chips()
    black_jack(chips, name, player)
    play_again = True
    while play_again is True:
        print('Do you want to play again? (y/n)')
        play = input('')
        if play.upper() != 'Y':
            play_again = False
        else:
            black_jack(chips, name, player)
    return 0


if __name__ == '__main__':
    main()
