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
is_user_hitting = True
is_dealer_hitting = True

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
def hit_or_stand(deck, hand_player):
    global is_user_hitting

    player_move = ''
    while player_move not in ['H', 'S']:
        player_move = input("Do you wan't to hit or stand (H/S)? ").upper()

    while True:
        if player_move[0].upper() == 'H':
            print("\nPlayer hits.")
            hit(deck, hand_player)
            show_player_cards(hand_player)
        elif player_move[0].upper() == 'S':
            print("\nPlayer stands.")
            is_user_hitting = False
        break
def show_player_cards(hand_player):
    print("\nPLAYER'S HAND")
    print("-------------")

    for card in hand_player.cards:
        print(card)

    print("-------------\n")
def show_table(player, dealer):
    print("\nPLAYER'S HAND")
    print("-------------")

    for card in player.cards:
        print(card)

    print("-------------")
    print("\nDEALER'S HAND")
    print("-------------")

    for card in dealer.cards:
        print(card)

    print("-------------\n")
def player_lost(player, dealer, chips):
    print("Player lost!")
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
def check_winner(hand_player, hand_dealer, player_chips):
    print("Check winner!")
    show_table(hand_player, hand_dealer)
    print(f"Player: {hand_player.value}")
    print(f"Dealer: {hand_dealer.value}")
    print(f"Chips Bet: {player_chips.bet}")
    print(f"Chips Total: {player_chips.total}")
    # if hand_dealer.value > 21:
    #     dealer_lost(hand_player, hand_dealer, player_chips)
    # elif hand_dealer.value > hand_player.value:
    #     dealer_won(hand_player, hand_dealer, player_chips)
    # elif hand_dealer.value < hand_player.value:
    #     player_won(hand_player, hand_dealer, player_chips)
    # else:
    #     push(hand_player, hand_dealer)

# Give player chips
player_chips = Chips()

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
    take_bet(player_chips)
    show_player_cards(hand_player)

    # Keep asking if the player wants to hit, until he stands or loses
    while is_user_hitting:
        hit_or_stand(deck, hand_player)

        if hand_player.value > 21:
            # player_lost(hand_player, hand_dealer, player_chips)
            is_dealer_hitting = False
            break

    # Keep dealer hitting until it's hand's value is under 17
    while is_dealer_hitting:
        print("\nDealer's turn!")

        while hand_dealer.value < 17:
            print("Dealer hits.")
            hit(deck, hand_dealer)

        print("Dealer stands.")
        is_dealer_hitting = False

    # Check for a winner or if the game was tied
    check_winner(hand_player, hand_dealer, player_chips)

    # print(f"Player's chips: {player_chips.total}\n")

    # Check if the player have enough chips and wants to play again
    if player_chips.total == 0:
        print("You lost all your chips! Thanks for playing!")
        break
    else:
        play_again = ''
        while play_again not in ['Y', 'N']:
            play_again = input("Would you like to play again (Y/N)? ").upper()

        if play_again[0] == 'Y':
            is_user_hitting = True
            is_dealer_hitting = True
            continue
        else:
            print("\nThanks for playing!")
            break
