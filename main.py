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

#Write your code below this line 👇

player = int(input("Type: 0 for Rock, 1 for the Paper, 2 Scissors."))
computer = random.randint(0,2)
total = player + computer
p = player
c = computer
if player != computer:
  if total == 2:
    if player == 2:
      player+= 5
    else:
      computer+= 5
  if player > computer:
    player+= 5
  else:
    computer+=5
else:
  print('''                                 >The Result is Draw! Lucky Human<''')
if p > c:
  print("                                           >Pathetic Human wins!<")
if c > p:
  print("                                          >Glorious Computer Wins!<")

if c == 2:
  print(scissors)
  print("Glorious Computer Wisely Chose The Scissors")
elif c == 1:
    print(paper)
    print("Glorious Computer Wisely Chose The Paper")
else:
  print(rock)
  print("Glorious Computer Wisely Chose The Rock")

if p == 2:
  print(scissors)
  print("Pathetic Human Randomly Chose The Scissors")
elif p == 1:
    print(paper)
    print("Pathetic Human Randomly Chose The Paper")
else:
  print(rock)
  print("Pathetic Human Randomly Chose The Rock")
  