#import the random package so we can generate a rando AI choice
from random import randint

# basket of choice
choices= ["rock", "paper", "scissors"]

#let the AI make a choice
	computer=choices[randint (0,2)]

	# set up a game loop here so we dont have to keep restating
	player = False 

	while player is False
	player=input ("choose rock, paper or scissors: \n")

	print("computer: ", computer "player: " player

# print (computer , player )
# 
# start doing some logic and condition checking 
# always check a breaking condition first
	if player == computer:
	# we have a tie , no pint in going any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print( " you chose to quit,quitter.")
		exit()

	elif: player== "rock":
		if computer == "paper":
			print("you lose!" , computer, "covers", player, "\n")
		else:
			print("you won!") , player, "smashes", computer, "\n"

	elif: player== "paper":
		if computer == "scissors":
			print("you lose!" , computer, "cuts", player, "\n")
		else:
			print("you won!") , player, "covers", computer, "\n"
	

	player = false\
	cpmuter = choices[ randit (0,2)]