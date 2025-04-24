import random
import os
import pdb

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN = 5
CENTER_SQUARE = 5

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]             # diagonals
    ]

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

    square = None

     # offense
    for line in WINNING_LINES:
            square = find_at_risk_square(line, board, COMPUTER_MARKER)
            if square:
                break
    # defense
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break

    # square 5
    if not square:
        if board[CENTER_SQUARE] == INITIAL_MARKER:
            square = CENTER_SQUARE
    
    # random
    if not square:
        square = random.choice(empty_squares(board))
    
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
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


def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

    

def play_tic_tac_toe():
    score = {
        'Player': 0,
        'Computer': 0
    }

    current_player = 'Player'
    
    while True: # match loop (best of 5)
    

        while score['Player'] < GAMES_TO_WIN and score['Computer'] < GAMES_TO_WIN:

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
            
            if score['Player'] == GAMES_TO_WIN or score['Computer'] == GAMES_TO_WIN:
                break


            prompt("Play again? (y or n)") # to play another round in match
            answer = input().lower()

            if answer[0] != 'y':
                break
            
            prompt('Thank you for playing Tic Tac Toe!')

        if GAMES_TO_WIN in score.values():
            prompt(f'{max(score)} won the match!')

            prompt("Play another match? (y or n)")
            answer = input().lower()

            if answer[0] != 'y':
                break

        break

    prompt('Thank you for playing Tic Tac Toe!')

play_tic_tac_toe()

# print(find_at_risk_square([1, 2, 3], {
#     1: COMPUTER_MARKER,
#     2: INITIAL_MARKER,
#     3: COMPUTER_MARKER,
#     4: INITIAL_MARKER,
#     5: INITIAL_MARKER,
#     6: INITIAL_MARKER,
#     7: COMPUTER_MARKER,
#     8: INITIAL_MARKER,
#     9: INITIAL_MARKER,
# }))




# print(join_or([1, 2, 3]))               # => "1, 2, or 3"
# print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
# print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
# print(join_or([]))                      # => ""
# print(join_or([5]))                     # => "5"
# print(join_or([1, 2]))                  # => "1 or 2"

'''
computer defense

Problem
Input: PLAYER has 2 squares in a row, 3rd empty
Output: "at-risk" square

Example

Data Structure
- Take "winning line's structure


# Algorithm

1. Given "winning_lines" nested list
2. For each line in "winning_lines"
3. if 2 square equal "HUMAN_MARKER" AND remaining square = "INITIAL_MARKER"
4. return 3rd square


{[1, 2]: 3}, [2, 3], [1, 3], [4, 5], [5, 6], [4, 6], [7, 8], [8, 9], [7, 9], # rows
        [1, 4], [4, 7], [1, 7], [2, 5], [5, 8], [2, 8], [3, 6], [6, 9], [3, 9], # columns
        [1, 5], [5, 9], [1, 9], [3, 5], [5, 7], [3, 7] # diagonals
    ]


    


'''