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

gameimg = [rock, paper, scissors]


import random

user = int(input("Let's play, choose your hand? Type 0 for rock, 1 for paper and 2 for scissors.\n "))

compumterhand = random.randint(0, 2)


if user >= 3 or user < 0:
    print("Invalid number, You Lose")
else:
    print(gameimg[user])
    print(f"computer chose {compumterhand}")
    print(gameimg [compumterhand])
   
    if user == 2 and compumterhand == 0:
        print("You Lose")
    elif compumterhand == 2 and user == 0:
        print("You Win")
    elif user > compumterhand:
        print("You Win")
    elif compumterhand > user:
        print("You Lose")
    elif user == compumterhand:
        print("It's a draw")
    elif user == 0 and compumterhand == 1:
        print("You Lose")
