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
import random
choices = ['rock', 'paper', 'scissors']
Computer_choice = random.choice(choices)
# print(Computer_choice)
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
if user_choice == '0':
    print('You chose :')
    print(rock)
    if Computer_choice == 'rock':
        print('Computer chose:\n', rock)
        print("It's a Draw")
    if Computer_choice == 'paper':
        print('Computer chose:\n', paper)
        print('You lose')
    if Computer_choice == 'scissors':
        print('Computer chose:\n', scissors)
        print('You win!')
if user_choice == '1':
    print('You chose :')
    print(paper)
    if Computer_choice == 'paper':
        print('Computer chose:\n', paper)
        print("It's a Draw")
    if Computer_choice == 'rock':
        print('Computer chose:\n', rock)
        print('You win!')
    if Computer_choice == 'scissors':
        print('Computer chose:\n', scissors)
        print('You lose')
if user_choice == '2':
    print('You chose :')
    print(scissors)
    if Computer_choice == 'scissors':
        print('Computer chose:\n', scissors)
        print("It's a Draw")
    if Computer_choice == 'paper':
        print('Computer chose:\n', paper)
        print('You win!')
    if Computer_choice == 'rock':
        print('Computer chose:\n', rock)
        print('You lose')
else:
    print('Invalid choice')