import random
from colorama import init, Fore, Style
init(autoreset=True)
# =========================================
# CONSTANTS (DO NOT EDIT)
# =========================================
win_conditions = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def display_board(board):
    """Prints the Tic-Tac-Toe board in color."""
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    """Asks player to choose X or O and returns (player_symbol, ai_symbol)."""
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).strip().upper()
    return ('X', 'O') if symbol == 'X' else ('O', 'X')

# ==========================================================
# TODO 1: player_move(board, symbol)
# ==========================================================
def player_move(board, symbol):
    # TODO: Ask for a move (1-9), validate empty spot, then place symbol
    pass

# ==========================================================
# TODO 2: ai_move(board, ai_symbol, player_symbol)
# ==========================================================
def ai_move(board, ai_symbol, player_symbol):
    # TODO A: Try to win in 1 move
    # TODO B: Try to block player win in 1 move
    # TODO C: Else, pick a random empty spot
    pass

# ==========================================================
# TODO 3: check_win(board, symbol)
# ==========================================================
def check_win(board, symbol):
    # TODO: Loop through WIN_COMBOS and return True if symbol wins
    pass

# ==========================================================
# TODO 4: check_full(board)
# ==========================================================
def check_full(board):
    # TODO: Return True if board has no digits left (all filled)
    pass

# ==========================================================
# MAIN GAME (NOW WITH A FEW TODOs)
# ==========================================================
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    # TODO (MAIN-1): Ask player's name in green and store it
    # Hint: if empty, default to "Player"
    name = None  # replace this line

    while True:
        # TODO (MAIN-2): Initialize the board as ["1","2",...,"9"]
        board = None  # replace this line

        # TODO (MAIN-3): Get symbols using player_choice()
        player_symbol, ai_symbol = None, None  # replace this line

        # TODO (MAIN-4): Decide who starts ("Player" or "AI")
        # Simple option: always start with Player
        turn = None  # replace this line

        while True:
            display_board(board)

            if turn == "Player":
                # TODO (MAIN-5): Call player_move() to place player's symbol
                # player_move(board, player_symbol)

                # TODO (MAIN-6): If player wins, print win message with name and break
                # if check_win(...):

                # TODO (MAIN-7): If tie (board full), print tie message and break
                # if check_full(...):

                # TODO (MAIN-8): Switch turn to "AI"
                pass

            else:
                # TODO (MAIN-9): Call ai_move() to place AI symbol
                # ai_move(board, ai_symbol, player_symbol)

                # TODO (MAIN-10): If AI wins, print AI win message and break
                # if check_win(...):

                # TODO (MAIN-11): If tie (board full), print tie message and break
                # if check_full(...):

                # TODO (MAIN-12): Switch turn to "Player"
                pass

        # TODO (MAIN-13): Ask "Play again? (yes/no): "
        # If answer is NOT "yes", print thank you and return
        again = None  # replace this line

if __name__ == "__main__":
    tic_tac_toe()