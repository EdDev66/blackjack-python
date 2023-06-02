import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def draw_cards(user, amount):
    for _ in range(amount):
        card = random.choice(cards)
        user.append(card)

def check_for_blackjack(cards):
    if 10 in cards and 11 in cards and len(cards) == 2:
        return True
    return False

def calculate_score(user_cards, pc_cards):

    user_blackjack = check_for_blackjack(user_cards)
    computer_blackjack = check_for_blackjack(pc_cards)

    if user_blackjack:
        if not computer_blackjack:
            return 2
        else:
            return 0
    elif computer_blackjack:
        if not user_blackjack:
            return 1
        else:
            return 0

    user_count = sum(user_cards)
    pc_count = sum(pc_cards)

    if 11 in user_cards and user_count > 21:
        nr_aces = user_cards.count(11)
        user_count -= 10 * nr_aces
    
    if 11 in pc_cards and pc_count > 21:
        nr_aces = pc_cards.count(11)
        pc_count -= 10 * nr_aces

    if user_count > 21:
            return 1
    elif pc_count > 21:
            return 2
    elif user_count == 21:
        return 1
    else:
        return 0
    
def check_winner(computer_cards, user_cards):

    result = calculate_score(user_cards, computer_cards)

    print('Your Cards: ', user_cards)
    print('Dealer Cards: ', computer_cards)

    user_count = sum(user_cards)
    computer_count = sum(computer_cards)

    if result == 0:
        if user_count > computer_count:
            print('You win!')
        elif computer_count > user_count:
            print('Dealer wins!')
        else:
            print("It's a draw!")
        
    if result == 1:
        print('Dealer wins!')

    if result == 2:
        print('You win!')

def reset_game():
    global user_cards 
    user_cards = []
    global computer_cards 
    computer_cards = []
    import os
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')
    clear_console()

def prompt_restart():
    restart_game = input('Type y to play again, anything else to quit: ')
    if restart_game == 'y':
        reset_game()
        start_game()
    else:
        exit()

def start_game():
    draw_cards(computer_cards, 2)
    draw_cards(user_cards, 2)

    while True:
        result = calculate_score(user_cards, computer_cards)
        
        print('Your Cards: ', user_cards)
        print('Dealer Cards: ', f"{computer_cards[0]}, 🂠")

        if result == 1:
            print('Bust!')
            print('Dealer wins!')
            prompt_restart()

        if result == 2:
            print('You win!')
            prompt_restart()

        hit_me = input('Type y to get another card, type anything else to pass: ')
        if hit_me == 'y':
            draw_cards(user_cards, 1)
        else:
            while sum(computer_cards) < 16:
                draw_cards(computer_cards, 1)
            check_winner(computer_cards, user_cards)
            prompt_restart()

print(art.logo)
start_game()