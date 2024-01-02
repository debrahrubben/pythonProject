import random

choices = ['rock','paper', 'scissors']
computer = random.choice(choices)
player = None
while player not in choices:
    player = input('Rock, Paper, Scissors?: ')
print('computer: ',computer)
print('player: ',player)

if computer == player:
    print('You guess right')
else:
    print('you failed to guess')

while player != computer:
    player = input('Rock, Paper, Scissors?: ')