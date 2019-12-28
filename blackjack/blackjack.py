from cards import shuffle,rank,suit
from players import Player, Dealer
from colors import Colors
import subprocess


# Instantiate player, dealer, and deck
player = Player()
dealer = Dealer()
deck = shuffle()

# Call to allow ANSI ESC codes for colors
subprocess.call('', shell=True)
# Ensure the colors are set to the default
color = Colors()
print(f"{color.norm}")


def main():

    # If the deck is low on cards, get a new deck
    global deck
    if len(deck) < 10:
        deck = shuffle()

    # Does the player have any money?
    if player.balance == 0:
        print("You're Broke!\n")
        quit()

    # Reset each player's cards
    player.card = []
    dealer.card = []

    # Play game
    place_bet(player)
    deal_cards(deck, player, dealer)
    player_turn()


def place_bet(player):
    """Bet on the hand"""

    while True:
        print(f"\n{color.cya}Balance:{color.norm} ${player.balance}")

        # Get a wager between 0 and the player's balance
        try:
            player.wager = input(f"{color.mag}('Q' to quit) {color.cya}Place your bet:{color.norm} $ ")
            if int(player.wager) > 0  and int(player.wager) <= player.balance:
                break
        
        # You can quit the game from here as well
        except:
            if player.wager == 'q':
                quit()

    # Wager must be an integer
    player.wager = int(player.wager)


def deal_cards(deck, player, dealer):
    """Deals the cards and checks for a blackjack"""

    # Ensures that one of the dealer's cards is hidden until the player is done
    dealer.initial = True

    # Deal the first four cards
    player.card.append(deck.pop())
    player.card.append(deck.pop())
    dealer.card.append(deck.pop())
    dealer.card.append(deck.pop())
    display_hand()

    # Check for a BlackJack
    if player.score() == 21 and dealer.score() == 21:
        print("It's a tie.\n")
        main()
    if player.score() == 21 and dealer.score() < 21:
        print(f"{color.grn}Blackjack, You won ${player.wager * 3}!{color.norm}\n")
        player.balance += player.wager * 3
        main()


def display_hand():
    """Displays both player's hands"""

    # Clear the screen
    print("\n" * 2)

    # Show dealer's hand. Hide one card if this is the initial deal
    print(f"{color.cya}Dealer{color.norm}  ", end="")
    if dealer.initial:
        print(f"{color.whtbg}{color.blk}  ?  {color.blkbg} {color.whtbg}{rank(dealer.card[1]):2}{suit(dealer.card[1])} {color.norm}", end="")
        print(f"\nTotal=??\n")
    else:
        for i in range(0, len(dealer.card)):
            print(f"{color.whtbg}{color.blk}{rank(dealer.card[i]):2}{suit(dealer.card[i])} {color.blkbg} {color.whtbg}{color.norm}", end="")
        print(f"\nTotal={dealer.score():2}\n")

    # Player's hand
    print(f"{color.cya}Player{color.norm}  ", end="")
    for j in range(0,len(player.card)):
        print(f"{color.whtbg}{color.blk}{rank(player.card[j]):2}{suit(player.card[j])} {color.blkbg} {color.whtbg}{color.norm}", end="")
    print(f"\nTotal={player.score():2}\n")


def player_turn():
    """Player is able to stand or take extra cards. Checks for a bust"""

    move = ""
    while move not in ['s', 'h']:

        # Get player's choice
        move = input(f"{color.cya}Bet ={color.norm} ${player.wager}  ({color.yel}H{color.norm})it or ({color.yel}S{color.norm})tand? ").lower()

        # Stand
        if move == 's':
            dealer_turn()

        # Hit me
        if move == 'h':
            player.card.append(deck.pop())

            # Check if busted
            if player.score() > 21:
                display_hand()
                print(f"{color.red}Busted! Dealer Wins{color.norm}\n")
                player.balance -= player.wager
                main()

            # Display hand and ask again
            display_hand()
            player_turn()


def dealer_turn():
    """Dealer hits on 16 and lower, stands on 17 and up. Checks for a bust"""

    # Turn of dealer.inital flag so that all dealer cards show in display_hand()
    dealer.initial = False

    # Hit if 16 or less
    if dealer.score() < 17:
        dealer.card.append(deck.pop())

        # Check if busted
        if dealer.score() > 21:
            display_hand()
            print(f"{color.grn}Dealer Busted! You won ${player.wager * 2}!{color.norm}\n")
            player.balance += player.wager * 2
            main()

        # Try again
        dealer_turn()

    # If total is 17 or higher, see who won
    else:
        check_win()


def check_win():
    """Compare scores, adjust the player's bankroll accordingly"""

    display_hand()

    if player.score() < dealer.score():
        print(f"{color.red}Dealer wins{color.norm}\n")
        player.balance -= player.wager
        main()

    elif player.score() > dealer.score():
        print(f"{color.grn}You won ${player.wager * 2}!{color.norm}\n")
        player.balance += player.wager * 2
        main()
        
    else:
        print("It's a tie.\n")
        main()



if __name__ == "__main__":
    main()
