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
is_playing = True;

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

    def __str__(self):

        deck_composition = ''
        for card in self.deck:
            deck_composition += f"\n{card.__str__()}"

        return 'The deck has:' + deck_composition

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
    def __init__(self, total = 100):
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
            chips.bet = int(input("How much do you want to bet (10 to 100)? "))
        except:
            print("Please provide a bet between 10 and 100!\n")
            continue
        else:
            if chips.bet < 10:
                print("The bet ammount must be between 10 and 100!\n")
                continue
            elif chips.bet > chips.total:
                print(f"You have just {chips.total} chips. Bet a smaller ammout!\n")
                continue
            else:
                break
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.aces_adjustment()
def hit_or_stand(deck, hand):
    global is_playing

    while True:
        player_choice = input("\nDo you wan't to hit or stand (H/S)? ")

        if player_choice[0].upper() == 'H':
            hit(deck, hand)
        elif player_choice[0].upper() == 'S':
            is_playing = False
        else:
            print("Please, type only H or S!")
            continue
        break
def show_some(player, dealer):
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)

    print("\nDealer's hand:")
    print("One card hidden!")
    print(dealer.cards[1])
def show_all(player, dealer):
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


# Game
while True:
    print("Welcome to Blackjack!\n")

    # Create the deck and shuffles it
    deck = Deck()
    deck.shuffle()

    # Create player's and dealer's hands, and adds two cards to each one
    hand_player = Hand()
    hand_dealer = Hand()
    hand_player.add_card(deck.deal())
    hand_player.add_card(deck.deal())
    hand_dealer.add_card(deck.deal())
    hand_dealer.add_card(deck.deal())

    # Give player initial chips and takes its bet ammount
    chips_player = Chips()
    take_bet(chips_player)

    # Show cards
    show_some(hand_player, hand_dealer)

    # Recall variable from hit_or_stand()
    while is_playing:
        # Check if player wants to hit or stand
        hit_or_stand(deck, hand_player)

        # Show cards
        show_some(hand_player, hand_dealer)

        if hand_player.value > 21:
            player_lost(hand_player, hand_dealer, chips_player)
            break

        # If the player didn's lost, play dealer's hand
        if hand_dealer.value <= 21:
            print("\nDealer's turn!")
            while hand_dealer.value < 17:
                hit(deck, hand_dealer)

            # Show cards
            show_all(hand_player, hand_dealer)

            # Test different winning scenarios
            if hand_dealer.value > 21:
                dealer_lost(hand_player, hand_dealer, chips_player)
            elif hand_dealer.value > hand_player.value:
                dealer_won(hand_player, hand_dealer, chips_player)
            elif hand_dealer.value < hand_player.value:
                player_won(hand_player, hand_dealer, chips_player)
            else:
                push(hand_player, hand_dealer)

        # Inform Player of their chips total
        print(f"Player's chips: {chips_player.total}")

        play_again = ''
        while play_again not in ('Y', 'N'):
            play_again = input("Would you like to play again (Y/N)? ")

        if play_again[0].upper() == 'Y':
            is_playing = True
            continue
        else:
            print("Thanks for playing!")
            break
