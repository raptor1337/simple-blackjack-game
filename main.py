import random
import sys

print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
\n\t\t\t-by raptor1337-\n""")

print("Welcome to BlackJack!\n\n")

computer_has = random.randint(6,19)
player_has = random.randint(6,19)



while True:
	print(f"\n\nComputer has {computer_has} points.")
	print(f"You have {player_has} points.")
	choice = input("\nHit Or Stand?: ")
	if choice.lower() == "hit":
		player_gets = random.randint(4,11)
		print(f"\nYou Got {player_gets} Points!")
		player_has = player_has + player_gets
		if player_has > 21:
			print(f"\nLooks Like You Passed 21... Game Over.")
			sys.exit(0)
		elif player_has == 21:
			print(f"\nBLACKJACK! You Won The Game! Congrats!")
			sys.exit(0)
	
	elif choice.lower() == "stand":
		pass

	computer_choice = random.randint(0,1)

	if computer_choice == 0:
		print("\nComputer Chose To Stand.\n")
	elif computer_choice == 1:
		computer_gets = random.randint(4,11)
		print(f"\nComputer Got {computer_gets} Points!")
		computer_has = computer_has + computer_gets
		if computer_has > 21:
			print(f"\nLooks Like Computer Passed 21. You Won The Game! Congrats!")
			sys.exit(0)
		elif computer_has == 21:
			print(f"\nBLACKJACK! You Lose! Game Over.")
			sys.exit(0)