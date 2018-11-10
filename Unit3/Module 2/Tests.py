# [ ] This project is an implementation a Tic Tac Toe game.
# The logic of the game is in the `main` function, read it before writing any code.

# Use the description and examples under each of the following functions to implement them:
# 1) draw(board)
# 2) available(location, board)
# 3) mark(player, location, board)
# 4) check_win(board)
# 5) check_tie(board)

from IPython.display import clear_output  # to clear the output (specific to Jupyter notebooks and ipython)
from random import randint


def draw(board):
    """
    Draw the `board` table.
    The board reflects the current state of the game, a number indicates an available location.
    args:
        board: 3x3 table (list of lists) containing the current state of the game
    returns:
        None
    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:
         7 | 8 | 9
        -----------
         4 | 5 | 6
        -----------
         1 | 2 | 3
         After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
         The printout should look like:
         7 | 8 | X
        -----------
         O | O | 6
        -----------
         1 | X | 3
    """
    i = 1
    for list in board:
        print(" " + list[0] + " | " + list[1] + " | " + list[2])
        if i < len(board):
            i += 1
            print("-----------")


def available(location, board):
    """
    Check the availability of a `location` on the current `board`

    An available location on the board contains a number between 1 and 9 stored as a string.
    If the location contains 'X' or 'O', the location is not available and the function should return False;
    otherwise, the function should return True indicating the location is available

    args:
        location: a number between 1 and 9 stored as a string
        board: 3x3 table (list of lists) containing the current state of the game

    returns:
        True if the location is available. False if the location is not available
    """
    all_values = []
    for list in board:
        for symbol in list:
            all_values += symbol
    if location in all_values:
        return True
    else:
        return False


def mark(player, location, board):
    """
    Mark `location` on the `board` with the `player` symbol.
    Should replace the `location` number on the board with `X` or `O`
    args:
        player: player's symbol, either 'X' or 'O'
        location: a number between 1 and 9 stored as a string
        board: 3x3 table (list of lists) containing the current state of the game
    returns:
        None
    """
    var1 = 0
    var2 = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == location:
                var1 = i
                var2 = j
    board[var1][var2] = player


def check_win(board):
    """
    Check if there is a winner.

    A win happens if the either of the players was able to place 3 symbols ('X' or 'O') in:
    a horizontal, vertical, diagonal, or anti-diagonal placement.

    args:
        board: 3x3 table (list of lists) containing the current state of the game

    returns:
        True if there is a winner. False if there is no winner yet

    examples:
        Horizontal win: +
        Vertical win:
        Diagonal win:
        Anti-Diagonal win:
        No winners yet:

    """
    sl = []
    for list in board:
        if (list[0] == "X" and list[1] == "X" and list[2] == "X") or (list[0] == "O" and list[1] == "O" and list[2] == "O"):
            return True
        else:
            pass
    for list in board:
        for symbol in list:
            sl += symbol

    if (sl[0] == "X" and sl[3] == "X" and sl[6] == "X") or (sl[0] == "O" and sl[3] == "O" and sl[6] == "O"):
        return True
    elif (sl[1] == "X" and sl[4] == "X" and sl[7] == "X") or (sl[1] == "O" and sl[4] == "O" and sl[7] == "O"):
        return True
    elif (sl[2] == "X" and sl[5] == "X" and sl[8] == "X") or (sl[2] == "O" and sl[5] == "O" and sl[8] == "O"):
        return True
    elif (sl[0] == "X" and sl[4] == "X" and sl[8] == "X") or (sl[0] == "O" and sl[4] == "O" and sl[8] == "O"):
        return True
    elif (sl[2] == "X" and sl[4] == "X" and sl[6] == "X") or (sl[2] == "O" and sl[4] == "O" and sl[6] == "O"):
        return True
    else:
        return False


def check_tie(board):
    """
    Check the game for a tie, no available locations and no winners.
    args:
        board: 3x3 table (list of lists) containing the current state of the game
    returns:
        True if there is a tie. False the board is not full yet or there is a winner
    """
    for list in board:
        for symbol in list:
            if (symbol != "X") or (symbol != "O"):
                return False

    if check_win(board) == True:
        return False
    else:
        return True


def dashes():
    """Print a fancy line of dashes"""
    print("o" + 35 * '-' + "o")


def display(message):
    """
    Print `message` in the center of a 35 characters string

    args:
        message: string to display

    returns:
        None
    """
    print("|{:^35s}|".format(message))


def main():
    # initializing game
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    # select the first player randomly
    player = ['X', 'O']
    turn = randint(0, 1)

    win = False
    tie = False
    while (not win and not tie):
        # switch players
        turn = (turn + 1) % 2

        clear_output()
        current_player = player[turn]  # contains 'X' or 'O'
        # display header
        dashes()
        display("TIC TAC TOE")
        dashes()

        # display game board
        print()
        draw(board)
        print()

        # display footer
        dashes()
        # player select a location to mark
        while True:
            location = input("|{:s} Turn, select a number (1, 9): ".format(current_player))
            if available(location, board):
                break  # Only the user input loop, main loop does NOT break
            else:
                print("Selection not available!")
        dashes()

        # mark selected location with player symbol ('X' or 'O')
        mark(current_player, location, board)

        # check for win
        win = check_win(board)

        # check for tie
        tie = check_tie(board)

    # Display game over message after a win or a tie
    clear_output()

    # display header
    dashes()
    display("TIC TAC TOE")
    dashes()

    # display game board (Necessary to draw the latest selection)
    print()
    draw(board)
    print()

    # display footer
    dashes()
    display("Game Over!")
    if (tie):
        display("Tie!")
    elif (win):
        display("Winner:")
        display(current_player)
    dashes()


# Run the game
main()