""" Functions related to the deck of cards
    The first digit is the suit.
    The last two digits are the card.
    1 = Ace, 11,12,13 = J, Q, K """

import random
from colors import Colors

color = Colors()

def shuffle():
    """ Returns a shuffled 52 card deck."""

    main_deck = [101,102,103,104,105,106,107,108,109,110,111,112,113,
                 201,202,203,204,205,206,207,208,209,210,211,212,213,
                 301,302,303,304,305,306,307,308,309,310,311,312,313,
                 401,402,403,404,405,406,407,408,409,410,411,412,413]

    # Make a copy of the deck so that the main_deck isn't affected
    new_deck = list(main_deck)

    # Shuffle the new deck
    random.shuffle(new_deck)

    return new_deck


def rank(card):
    """ Returns the rank of a card. Converts A,J,Q,K to alpha """

    if card % 100 == 1:
        return ' A'
    elif card % 100 == 11:
        return ' J'
    elif card % 100 == 12:
        return ' Q'
    elif card % 100 == 13:
        return ' K'
    else:
        return card % 100


def suit(card):
    """ Returns a unicode graphic of the suit based on the first number """

    # Clubs
    if card in range(100,114):
        return " \u2663"
    # Diamonds
    elif card in range(200,214):
        return f" {color.red}\u2666{color.blk}"
    # Hearts
    elif card in range(300,314):
        return f" {color.red}\u2665{color.blk}"
    # Spades
    else:
        return " \u2660"
