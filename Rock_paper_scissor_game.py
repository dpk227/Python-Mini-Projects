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
choice = input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n")
choicenum = int(choice) -1
computer_choice = random.randint(0,2)
if choicenum == 0:
  if computer_choice == 0:
    print(f"You chose:\n{rock}\nComputer chose:\n{rock}\nIt's a draw.")
  elif computer_choice == 1:
    print(f"You chose:\n{rock}\nComputer chose:\n{paper}\nYou lose.")
  elif computer_choice == 2:
    print(f"You chose:\n{rock}\nComputer chose: \n{scissors}\nYou win.")
if choicenum == 1:
  if computer_choice == 1:
    print(f"You chose:\n{paper}\nComputer chose:\n{paper}\nIt's a draw.")
  elif computer_choice == 2:
    print(f"You chose:\n{paper}\nComputer chose:\n{scissors} \nYou lose.")
  elif computer_choice == 0:
    print(f"You chose:\n{paper}\nComputer chose: \n{rock}\nYou win.")
if choicenum == 2:
  if computer_choice ==2:
    print(f"You chose:\n{scissors}\nComputer chose:\n{scissors}\nIt's a draw.")
  elif computer_choice ==1:
    print(f"You chose:\n{scissors}\nComputer chose:\n{paper}\nYou win")
  elif computer_choice == 0:
    print(f"You chose:\n{scissors}\nComputer chose: \n{rock}\nYou lose.")