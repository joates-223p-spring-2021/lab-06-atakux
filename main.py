# -*- coding: utf-8 -*-
"""

Angela DeLeo
CPSC 223P-01
Tue Mar 07 19:42:12 2021
atakux707@csu.fullerton.edu

"""




#things to do for the program:
"""
1. create randomized pc weapon choices
2. receive user input, check if invalid
	a. R = rock
	b. P = paper
	c. S = scissor
	d. Q = quit
	e. invalid input = retry
3. check the outcomes
	a. rock smashes scissors
	b. scissors slices paper
	c. paper covers rock
	d. same weapon = tie
4. display outcomes
5. keep track of pc wins, player wins, and ties
6. once player inputs Q
	a. end loop
	b. display final tally
		- computer: score
		- player(you) : score
		- ties: score
		- outcome: who won
"""

import random


#declare user and computer stuff
userChoice = ""
pcWeapon = ""

#start the tallies at 0
pcWins = 0
userWins = 0
ties = 0



while userChoice != 'q':
	userChoice = input("Make your choice: (R, P, S, Q) > ").lower()

	#random int for pc weapon
	pcRand = random.randint(0, 2)

	if pcRand == 0:
		pcWeapon = 'rock'
	elif pcRand == 1:
		pcWeapon = 'paper'
	elif pcRand == 2:
		pcWeapon = 'scissors'


	#check user's input and begin tallying

	if userChoice == 'q':
		break
	
	elif userChoice == pcWeapon[0]:
		ties += 1
		print("Computer chose {0}. Call it a draw.".format(pcWeapon.title()))

	elif userChoice == 'r':
		if pcWeapon == 'paper':
			pcWins += 1
			print("Computer chose {0}. Computer wins!".format(pcWeapon.title()))
		else:
			userWins += 1 
			print("Computer chose {0}. You win!".format(pcWeapon.title()))
	
	elif userChoice == 'p':
		if pcWeapon == 'rock':
			userWins += 1
			print("Computer chose {0}. You win!".format(pcWeapon.title()))
		else:
			pcWins += 1
			print("Computer chose {0}. Computer wins!".format(pcWeapon.title()))
	elif userChoice == 's':
		if pcWeapon == 'paper':
			userWins += 1
			print("Computer chose {0}. You win!".format(pcWeapon.title()))
		else:
			pcWins += 1
			print("Computer chose {0}. Computer wins!".format(pcWeapon.title()))		
	else:
		print("Invalid entry. Try Again")


print(f"Computer: {pcWins}\nYou: {userWins}\nTies: {ties}")
#display the outcomes

if pcWins > userWins:
	print("Computer won!")
elif pcWins < userWins:
	print("You won!")
elif pcWins == userWins:
	print("You tied!")
