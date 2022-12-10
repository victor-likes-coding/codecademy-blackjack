from models.Game import Card, Game

"""
  Purpose of this program is to facilitate a game of blackjack
  What is needed to accomplish this are the following models:
    * Card
    * Hand
    * Deck
    * Player
    * Dealer
    * Bank
    - Game

    Card: represents a single card and logic associated to a card
      * 2 cards combined will become a Hand
      * Cards will be able to give it's value
      * It should be able to provide feedback if instantiated with wrong value
        * wrong values being 2 > x > 9 (less than 2 and greater than 9)
        * a letter that isn't A, J, Q, K
        * If a card is an Ace card or 'A' it should be able to determine when to be a 1 or 11 with the help of a Hand

    Hand: represents a player's hand
      * Can hold up to 5 cards and only supports having type Card in it
      * Should be able to add a card to itself
      * Should be able to determine's it's own length
      * Should be indexable, meaning I can grab the 0th card

    Deck: represents a list of 52 cards, 2*9, J, Q, K, A one set per symbol Club, Spade, Diamond, Hearts
      * Should be able to shuffle
      * Should be able to perform a cut (take 1/4 or 1/2 and take bottom and place on top of itself)
      * Should be able to be drawn
      * Should be able to tell how many cards are left in the in itself
      * Should be indexable
      * Should be sliceable

    Player: represents the human player making choices about life
      * Should have a balance
      * Should have a hand
      * Should know how many times they've won
      * should know how many times they've lost
      actions:
        ! these all belong to the game of blackjack
        ! surrender: give up against the dealer
        ! hit: get another card
        ! double: double the bet
        ! split: split into 2 hands if they have doubles (not implemting)
        ! cash out: leave with their earnings or lack thereof
        ! load up: increase balance (maximum free credit $100)

    Dealer: represents the House in the game (doesn't need to be implemented)
      * Should have a hand
      * Should know how many times they've won
      * should know how many times they've lost

    Bank: represents the House's money in the game
      * should have a balance (1,000,000,000 default)
      ? automatically gain/lose balance when player cashes out

    Game: represents the game simulation itself
      - should have a list of players (8 max)
      actions:
        - set up the game (set_up)
          - get initial bet from players
          - have deck deal to players
        - play
          - go through each player allowing them to perform actions
            - hit
            - double
            - surrender
        - dealer_plays
          - dealer will decide to hit or not

"""

# this is the AI generated code for Game

# Import the random module for shuffling the deck
import random

# Define a list of suits
suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

# Define a list of ranks
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

# Define a dictionary mapping ranks to their corresponding values
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

# Define a function to shuffle the deck


def shuffle_deck():
    # Create a new deck of cards
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + ' of ' + suit)
    # Shuffle the deck
    random.shuffle(deck)

    return deck

# Define a function to calculate the total value of a hand of cards


def calculate_total(hand):
    # Calculate the total value of the hand
    total = 0
    for card in hand:
        total += values[card.split(' of ')[0]]

    # Check for an Ace in the hand and adjust the total if necessary
    for card in hand:
        if card.split(' of ')[0] == 'Ace':
            if total > 21:
                total -= 10

    return total

# Define a function to deal a card to a player


def deal_card(deck, hand):
    # Pop the top card from the deck and add it to the hand
    card = deck.pop()
    hand.append(card)

# Define a function to print the current state of the game


def show_table(player_hand, dealer_hand, dealer_showing):
    # Print the player's hand
    print('Your hand:')
    for card in player_hand:
        print(card)
    print('Total:', calculate_total(player_hand))
    print()

    # Print the dealer's hand
    print('Dealer\'s hand:')
    for i in range(dealer_showing):
        print(dealer_hand[i])
    print('Total:', calculate_total(dealer_hand[:dealer_showing]))
    print()
# Define a function to play a game of blackjack


def play_game():
    # Shuffle the deck
    deck = shuffle_deck()

    # Deal the initial cards
    player_hand = []
    dealer_hand = []
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)

    # Print the initial state of the game
    show_table(player_hand, dealer_hand, 1)

    # Prompt the player to hit or stay
    choice = input('Hit or stay? (h/s) ')

    # Keep dealing cards to the player until they choose to stay or bust
    while choice == 'h':
        # Deal a card to the player
        deal_card(deck, player_hand)

        # Print the current state of the game
        show_table(player_hand, dealer_hand, 1)

        # Check if the player has busted
        if calculate_total(player_hand) > 21:
            print('You bust!')
            break

        # Prompt the player to hit or stay again
        choice = input('Hit or stay? (h/s) ')

    # If the player hasn't bust, play the dealer's hand
    if calculate_total(player_hand) <= 21:
        # Reveal the dealer's hand
        show_table(player_hand, dealer_hand, len(dealer_hand))

        # Keep dealing cards to the dealer until they have at least 17 points
        while calculate_total(dealer_hand) < 17:
            deal_card(deck, dealer_hand)
            show_table(player_hand, dealer_hand, len(dealer_hand))

        # Check if the dealer has busted
        if calculate_total(dealer_hand) > 21:
            print('Dealer busts!')

        # Compare the player's and dealer's hands and determine the winner
        elif calculate_total(dealer_hand) >= calculate_total(player_hand):
            print('Dealer wins!')
        else:
            print('You win!')


def main():
    play_game()


if __name__ == '__main__':
    main()
