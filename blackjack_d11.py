from Blackjack_art import logo
import random
import sys, subprocess
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """returns a random card from the deck"""
    card = random.choice(cards)
    return card

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    def calculate_score(cards):
        """Takes from a list of cards and returns the score calculated from the cards"""
        # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return("It's a draw :|")
        elif computer_score == 0:
            return("You lose, opponent has Blackjack :(")
        elif user_score == 0:
            return("You win with a Blackjack! :D")
        elif user_score > 21:
            return("You went over, you lose :(")
        elif computer_score > 21:
            return("Opponent went over, you win! :D")
        elif computer_score > user_score:
            return("Opponent has higher score, you lose :(")
        else:
            return ("You have higher score, you win! :D")


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
    #while loop for user
        user_score = (calculate_score(user_cards))
        computer_score = (calculate_score(computer_cards))

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
    #while loop for computer
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    subprocess.run('cls', shell=True)
    play_game()

