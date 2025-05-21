import random


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

Choice=input("Rock, Paper, Scissors").lower()
botchoice = random.choice([rock, paper, scissors])

if Choice == "rock":
    print(rock)
    if botchoice == rock:
        print(botchoice)
        print('Draw!')
    elif botchoice == paper:
        print(botchoice)
        print('You lose!')
    elif botchoice == scissors:
        print(botchoice)
        print('You win!')
    else:
        print('Hm, not sure what just happened dawg')
elif Choice == "paper":
    print(paper)
    if botchoice == rock:
        print(botchoice)
        print('You win!')
    elif botchoice == paper:
        print(botchoice)
        print('Draw!')
    elif botchoice == scissors:
        print(botchoice)
        print('You Lose!')
    else:
        print('Hm, not sure what just happened dawg')
elif Choice == "scissors":
    print(scissors)
    if botchoice == rock:
        print(botchoice)
        print('You Lose!')
    elif botchoice == paper:
        print(botchoice)
        print('You Win!')
    elif botchoice == scissors:
        print(botchoice)
        print('Draw!')
    else:
        print('Hm, not sure what just happened dawg')
else:
    print("I'm sorry, I said Rock, Paper, Scissors'")
