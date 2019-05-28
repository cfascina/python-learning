import random
from os import system, name

# Global Variables
suits = (
    'Hearts',
    'Diamonds',
    'Spades',
    'Clubs')
symbols = (
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
    'A')
values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11}
is_user_hitting = True;

# Classes
class Card():
    def __init__(self, suit, symbol):
        self.suit = suit
        self.symbol = symbol

    def __str__(self):
        return f"{self.symbol} of {self.suit}"
class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.symbol]

        if card.symbol == 'A':
            self.aces += 1;

    def aces_adjustment(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips():
    def __init__(self, total = 150):
        self.total = total
        self.bet = 0

    def bet_won(self):
        self.total += self.bet

    def bet_lost(self):
        self.total -= self.bet

# Functions
def clear_console():
    if name == 'nt': # For Windows
        _ = system('cls')
    elif(name == 'posix'): # For Linux and MacOS
        _ = system('clear')
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f"How much do you want to bet (1 to {chips.total})? "))
        except:
            print(f"Please provide a bet between 1 and {chips.total}!\n")
            continue
        else:
            if chips.bet < 1:
                print(f"The bet ammount must be between 1 and {chips.total}!\n")
                continue
            elif chips.bet > chips.total:
                print(f"You don't have enough chips. Bet a smaller ammout!\n")
                continue
            else:
                break
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.aces_adjustment()
def hit_or_stand(deck, hand):
    global is_user_hitting

    player_move = ''
    while player_move not in ['H', 'S']:
        player_move = input("Do you wan't to hit or stand (H/S)? ").upper()

    while True:
        if player_move[0].upper() == 'H':
            print("\nPlayer hits.")
            hit(deck, hand)
        elif player_move[0].upper() == 'S':
            print("\nPlayer stands.")
            is_user_hitting = False
        break
def show_cards(player, dealer):
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)

    print("\nDealer's hand:")
    print("One card hidden!")
    print(f"{dealer.cards[1]}\n")
def show_all_cards(player, dealer):
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)

    print("\nDealer's hand:")
    for card in dealer.cards:
        print(card)
def player_lost(player, dealer, chips):
    print("Player Lost!")
    chips.bet_lost()
def player_won(player, dealer, chips):
    print("\nPlayer Won!")
    chips.bet_won()
def dealer_lost(player, dealer, chips):
    print("\nDealer Lost!")
    chips.bet_lost()
def dealer_won(player, dealer, chips):
    print("\nDealer Won!")
    chips.bet_won()
def push(player, dealer):
    print("\nGame Tied!")

# Give player chips
chips_player = Chips()

# Start the game
while True:
    clear_console()
    print("Welcome to Blackjack!\n")

    # Create the deck and shuffles it
    deck = Deck()
    deck.shuffle()

    # Create player's and dealer's hands
    hand_player = Hand()
    hand_dealer = Hand()

    # Add two cards to each one
    hand_player.add_card(deck.deal())
    hand_player.add_card(deck.deal())
    hand_dealer.add_card(deck.deal())
    hand_dealer.add_card(deck.deal())

    # Take player's bet and show the cards
    take_bet(chips_player)
    show_cards(hand_player, hand_dealer)

    # While player is hitting, add cards to his hand and shows the table
    while is_user_hitting:
        hit_or_stand(deck, hand_player)
        show_cards(hand_player, hand_dealer)

        if hand_player.value > 21:
            player_lost(hand_player, hand_dealer, chips_player)
            break

    print(f"Player's chips: {chips_player.total}\n")

    # Check if the player have enough chips and wants to play again
    if chips_player.total == 0:
        print("You lost all your chips! Thanks for playing!")
        break
    else:
        play_again = ''
        while play_again not in ['Y', 'N']:
            play_again = input("Would you like to play again (Y/N)? ").upper()

        if play_again[0] == 'Y':
            continue
        else:
            print("\nThanks for playing!")
            break
