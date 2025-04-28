import random
import copy
import os

SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
# VALUES = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace')
# ROYAL_ACE_VALUES = {
#     ('Jack', 'Queen', 'King'): 10,
#     'Ace': [1, 11]
# }
# DECK = {suit: VALUES for suit in SUITS}

VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
          'Jack', 'Queen', 'King', 'Ace']

DECK = [[suit, value] for suit in SUITS
        for value in VALUES]

game_deck = copy.deepcopy(DECK)


GAME_LIMIT = 21
DEALER_LIMIT = 17
CARDS_INITIAL_DEAL = 2

# print(DECK)

def initialize_deck():
    return copy.deepcopy(DECK)

def prompt(message):
    print(f'==> {message}')

def deal(hand, deck): # use a list of the existing hand
    drawn_card = deck.pop()[1]
    hand.append(drawn_card)

def initial_deal(player, dealer, deck):
    for _ in range(CARDS_INITIAL_DEAL):
        deal(player, deck)
        deal(dealer, deck)

def join_and(lst, delimiter=', ', join_word='and'):
    str_lst = [str(num) for num in lst]
    
    joined_nums = ''

    if len(str_lst) == 0:
        return joined_nums
    
    if len(str_lst) == 1:
        joined_nums += str_lst[0]
        return joined_nums
    
    joined_nums += delimiter.join(str_lst[:-1])
    return f'{joined_nums} {join_word} {str_lst[-1]}'

def display_hidden_hands(dealer, player):
#    dealer_values = [dealer[idx][1] for idx in range(len(dealer)) if idx > 0]
#    dealer_values = ','.join(dealer_values)
   prompt(f'Dealer has: {join_and(dealer[1:])} and unknown card')
   prompt(f'You have: {join_and(player)}') 


    
def total(cards):
    
    values = [card for card in cards]
    
    sum_values = 0

    for value in values:
        if value == 'Ace':
            sum_values += 11

        elif value in ['Jack', 'Queen', 'King']:
            sum_values += 10

        else:
            sum_values += int(value)

    aces_count = values.count('Ace')
    while aces_count and sum_values > GAME_LIMIT:
        sum_values -= 10
        aces_count -= 1

    return sum_values

    


def busted(hand):
    return total(hand) > GAME_LIMIT

def player_turn(hand, deck):
    
    while True:
        answer = input('Hit or stay? ')
        while answer.casefold() not in ['hit', 'stay', 'h', 's']:
            prompt("That's not a valid answer, please enter 'hit' or 'stay'")
            answer = input('Hit or stay?')

        
        if answer.casefold()[0] == 'h':

            deal(hand, deck)

            print(hand)       

            if busted(hand):
                winner = 'dealer'
                prompt(f'The winner is {winner}')

            break

        else:
            prompt("You chose to stay!")
            break



        

    # if total(player) > LIMIT:
    #     # end game? 
    #     busted = True


def dealer_turn(hand, deck):
    while hand <= DEALER_LIMIT:
        deal(hand, deck)
    
    
def shuffle(deck):
    random.shuffle(deck)

def play_again():
    prompt("Play again? (y or n)") # returns Boolean
    answer = input().strip()
    while answer not in ['y', 'Y', 'n', 'N']:
        prompt("That's not a valid choice: please enter 'y' or 'n' ")
        answer = input()

    if answer[0].casefold() != 'y':
        return False   
    
    return True

def play_twenty_one():
        
    while True:
        os.system('clear')
        
        player_hand = []
        dealer_hand = []

        deck = initialize_deck()
        shuffle(deck)

        initial_deal(player_hand, dealer_hand, deck)

        print(player_hand)
        print(dealer_hand)
        print(f'Player total is {total(player_hand)}')

        # prompt(f'Dealer has: {dealer_hand[1][1]} and unknown card')
        # prompt(f'You have: {player_hand[0][1]} and {player_hand[1][1]}')
        display_hidden_hands(dealer_hand, player_hand)

        while True:
            player_turn(player_hand, deck)
            
            if busted(player_hand):
                display_hidden_hands(dealer_hand, player_hand)
                break
            
            break # if chose to stay

            os.system('clear')
            display_hidden_hands(dealer_hand, player_hand)

        dealer_turn(dealer_hand, deck)

        if not play_again():
            break

            

    prompt('Thank you for playing twenty-one!')

play_twenty_one()

# print(total(['Queen', '2', 'Queen']))
# print(busted(['Queen', '2', 'Queen']))

# print(DECK)




