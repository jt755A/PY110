import random
import copy
import os
import time

SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
          'Jack', 'Queen', 'King', 'Ace']
DECK = [[suit, value] for suit in SUITS
        for value in VALUES]
GAME_LIMIT = 21
DEALER_LIMIT = 17
NUM_CARDS_INITIAL_DEAL = 2

game_deck = []
player_hand = []
dealer_hand = []

def initialize_deck():
    return copy.deepcopy(DECK)

def prompt(message):
    print(f'==> {message}')

def deal(hand): # use a list of the existing hand
    drawn_card = game_deck.pop()[1]
    hand.append(drawn_card)

def initial_deal(player, dealer):
    # Takes card from end of deck, deals alternately to player and dealer
    for _ in range(NUM_CARDS_INITIAL_DEAL):
        deal(player)
        deal(dealer)

def join_and(lst, delimiter=', ', join_word='and', hidden=False):
   
    joined_nums = ''
    
    if not hidden:
        str_lst = [str(num) for num in lst]
        joined_nums += delimiter.join(str_lst[:-1])
        return f'{joined_nums} {join_word} {str_lst[-1]}'
    
    elif hidden:
        str_lst = [str(num) for num in lst[1:]]

        if len(str_lst) == 1:
            return str_lst[0]
                     
        joined_nums += delimiter.join(str_lst[:])
        return f'{joined_nums} and unknown card'


def display_hidden_hands():
   prompt(f'Dealer has: {join_and(dealer_hand, ', ', 'and', True)} '
          f'and unknown card')
   prompt(f'You have: {join_and(player_hand)}')
   prompt(f'Player total is {total(player_hand)}')

def reveal_hands():
    # print('\n\n')
    # prompt('The final result is:')
    prompt(f'Dealer has: {join_and(dealer_hand)}. '
           f'Dealer total is {total(dealer_hand)}')
    prompt(f'You have: {join_and(player_hand)}. '
           f'Player total is {total(player_hand)}')
    
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

def player_turn():
    
    while True:
        answer = input('Hit or stay? ')
        while answer.casefold() not in ['hit', 'stay', 'h', 's']:
            prompt("That's not a valid answer, please enter 'hit' or 'stay'")
            answer = input('Hit or stay? ')

        
        if answer.casefold()[0] == 'h':

            deal(player_hand)
            prompt(f'Player now has: {join_and(player_hand)}')
            prompt(f'Your total is now: {total(player_hand)}')
            # display_hidden_hands()

            if busted(player_hand):
                return
                        
        else:
            prompt(f"You chose to stay at {total(player_hand)}!")
            break

def dealer_turn():
    while total(dealer_hand) <= DEALER_LIMIT:
        prompt(f'The dealer hits.')
        time.sleep(2)
        deal(dealer_hand)
        # prompt(f'Dealer has: {join_and(dealer_hand[1:], ',', ',')} and unknown card')
        prompt(f'Dealer now has: {join_and(dealer_hand, ', ', 'and', True)}')
          #f'and unknown card')

        if busted(dealer_hand):
            return
            # busted_ = True
            # return busted_
    
    time.sleep(2)
    prompt(f'The dealer stays at {total(dealer_hand)}')

def compare_cards():
    print('==========================================')
    reveal_hands()


    if total(player_hand) < total(dealer_hand):
        prompt('Dealer wins!')
    elif total(player_hand) > total(dealer_hand):
        prompt('Player wins!')
    else:
        prompt("It's a tie!")    
    
def shuffle(deck):
    random.shuffle(deck)

def play_again():
    prompt("Would you like to play again? (y or n)")
    answer = input().strip()
    while answer.casefold() not in ['y', 'yes', 'n', 'no']:
        prompt("That's not a valid choice: please enter 'y' or 'n' ")
        answer = input()

    if answer[0].casefold() != 'y':
        return False   
    
    return True

def play_twenty_one():
        
    while True:
        # outer game loop
        while True:
            # inner game loop: for play again? question
            os.system('clear')
            game_deck.clear()
            
            player_hand.clear()
            dealer_hand.clear()

            game_deck.extend(initialize_deck())
            shuffle(game_deck)

            initial_deal(player_hand, dealer_hand)

            # print(f'Player hand: {player_hand}')
            # print(f'Dealer hand: {dealer_hand}')
            # print(f'Player total is {total(player_hand)}')
        
            display_hidden_hands()

            player_turn()
                
            if busted(player_hand):
                prompt('Player busted. Dealer wins!')
                reveal_hands()
                break

            dealer_turn()

            if busted(dealer_hand):
                prompt('Dealer busted. Player wins!')
                reveal_hands()
                break

            compare_cards()
            break

        time.sleep(3)
        if not play_again():
            break            

    prompt('Thank you for playing twenty-one!')

play_twenty_one()
