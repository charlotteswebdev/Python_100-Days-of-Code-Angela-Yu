rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

error = '''
                                     \ / _
                                      ___,,,
                                      \_[o o]
     Errare humanum est!              C\  _\/
             /                     _____),_/__
        ________                  /     \/   /
      _|       .|                /      o   /
     | |       .|               /          /
      \|       .|              /          /
       |________|             /_        \/
       __|___|__             _//\        \
 _____|_________|____       \  \ \        \
                    _|       ///  \        \
                   |               \       /
                   |               /      /
                   |              /      /
 ________________  |             /__    /_
 b'ger        ...|_|.............. /______\.......
'''

import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print(f"You typed an invalid number, you lose! {error}")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {computer_choice}")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw")