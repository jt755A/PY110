import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN = 5

def prompt(message):
    print(f'==> {message}')

def display_board(board):
    os.system('clear')

    prompt(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')

    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}"),
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}"),
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}"),
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(lst, delimiter=', ', join_word='or'):
    str_lst = [str(num) for num in lst]
    
    joined_nums = ''

    if len(str_lst) == 0:
        return joined_nums
    
    if len(str_lst) == 1:
        joined_nums += str_lst[0]
        return joined_nums
    
    joined_nums += delimiter.join(str_lst[:-1])
    return f'{joined_nums} {join_word} {str_lst[-1]}'
           
def player_chooses_square(board):
    # valid square choices are those board keys whose values are spaces

    while True:        
        valid_choices = [str(num) for num in empty_squares(board)]
        # prompt(f'Choose a square ({', '.join(valid_choices)}):')
        prompt(f'Choose a square ({join_or(valid_choices)}):')


        square = input().strip()
        if square in valid_choices:
            break # break if it's a valid square

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
       return

    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]             # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
              and board[sq2] == COMPUTER_MARKER
              and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None

def play_tic_tac_toe():
    score = {
        'Player': 0,
        'Computer': 0
    }
    
    
    while True:

        while score['Player'] < 5 and score['Computer'] < 5:

            board = initialize_board()

            while True:
                display_board(board)

                player_chooses_square(board)

                if someone_won(board) or board_full(board):
                    break

                computer_chooses_square(board)

                if someone_won(board) or board_full(board):
                    break

            
            if someone_won(board):
                prompt(f'{detect_winner(board)} won!')
                score[detect_winner(board)] += 1
                
            else:
                prompt("It's a tie!")

            prompt(f'The score is: Player: {score['Player']}'
                   f' Computer: {score['Computer']}')


        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break
        
        prompt('Thank you for playing Tic Tac Toe!')

play_tic_tac_toe()

# print(join_or([1, 2, 3]))               # => "1, 2, or 3"
# print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
# print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
# print(join_or([]))                      # => ""
# print(join_or([5]))                     # => "5"
# print(join_or([1, 2]))                  # => "1 or 2"

