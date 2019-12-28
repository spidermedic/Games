"""Simple command line tic-tac-toe game"""

import sys

# initalize board. c[0] is used as a counter
c = [0,' ',' ',' ',' ',' ',' ',' ',' ',' ']


def main():
    """ Main function """
    
    draw_board()
    player1()


# Player 1's turn
def player1():
    """Player 1's turn"""

    p1=''
    while not p1.isdigit() or int(p1) not in range(1,9):
        p1 = input('Player 1 (X): ')
    p1 = int(p1)
    if c[p1] == " ":
        c[p1] = 'X'
        draw_board()
        check_win('X')
        player2()


# Player 2's turn
def player2():
    """Player 2's turn"""

    p2=''
    while not p2.isdigit() or int(p2) not in range(1,9):
        p2 = input('Player 2 (O): ')
    p2 = int(p2)
    if c[p2] == " ":
        c[p2] = 'O'
        draw_board()
        check_win('O')
        player1()


# See if the last move resulted in a win
def check_win(s):

    # Increment c[0] to count number of moves
    c[0] += 1

    # Check winning combinations
    if (c[1] == c[2] == c[3] == s) or \
       (c[4] == c[5] == c[6] == s) or \
       (c[7] == c[8] == c[9] == s) or \
       (c[1] == c[4] == c[7] == s) or \
       (c[2] == c[5] == c[8] == s) or \
       (c[3] == c[6] == c[9] == s) or \
       (c[3] == c[5] == c[7] == s) or \
       (c[1] == c[5] == c[9] == s):
        draw_board()
        sys.exit(f'\n* * * {s} has won the game! * * *\n')

    # if c[0] == 9 and there is no winnder, then announce draw
    if c[0] == 9:
        draw_board()
        sys.exit(f'\n* * * The game is a draw! * * *\n')

    # No winner, not a draw, continue game
    else:
        if s == 'X':
            player2()
        else:
            player1()

# Draw/update the board
def draw_board():


    print('\n' * 20)
    print(f' {c[7]} │ {c[8]} │ {c[9]} \t  7 │ 8 │ 9 ')
    print(f'───┼───┼─── \t ───┼───┼───')
    print(f' {c[4]} │ {c[5]} │ {c[6]} \t  4 │ 5 │ 6 ')
    print(f'───┼───┼─── \t ───┼───┼───')
    print(f' {c[1]} │ {c[2]} │ {c[3]} \t  1 │ 2 │ 3 \n')


if __name__ == '__main__':
    main()
