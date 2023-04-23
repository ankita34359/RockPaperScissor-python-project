# Importing random module
import random 

# Computer and User are selecting their moves
user_choice = input("Pick your move[Rock, Paper, Scissor]:")

# random.choice(["Rock", "Ppaer", "Scissor"])
# This command will pick a string randomly from 'Rock', 'Ppaer', 'Scissor' and assign it to the computer choice variable

computer_choice = random.choice(["rock", "paper", "scissor"])

# Print the taken input
print('user_choice :' , user_choice)
print("computer_choice:" , computer_choice)

# Conditions

if user_choice =="rock" and  computer_choice == "rock":
  print("DRAW")
elif user_choice =="rock" and  computer_choice == "paper":
  print("COMPUTER WON")
elif user_choice =="rock" and  computer_choice == "scissor":
  print("USER WON")
elif user_choice =="paper" and  computer_choice == "rock":
  print("USER WON")
elif user_choice =="paper" and  computer_choice == "paper":
  print("DRAW")
elif user_choice =="paper" and  computer_choice == "scissor":
  print("COMPUTER WON")
elif user_choice =="scissor" and  computer_choice == "rock":
  print("COMPUTER WON")
elif user_choice =="scissor" and  computer_choice == "paper":
  print("USER WON")
elif user_choice =="scissor" and  computer_choice == "scissor":
  print("DRAW")
else:
  print("Invalid case")











'''
number1 = 2
number2 = 3

# The working of "AND" operator 

print(number1 == 2 and number2 == 3)
print(number1 == 3 and number2 == 2)
print(number1 == 2 and number2 == 2)
print(number1 == 3 and number2 == 3)


# The working of "OR" operator

print(number1 == 2 or number2 == 3 )
print(number1 == 2 or number2 == 2 )
print(number1 == 3 or number2 == 3 )
print(number1 == 3 or number2 == 2 )

'''  


