import random
from start_game import startGame
from exit_game import exitGame

def singlePlayer():
	"""
	Controls the game play for a single player
	:return: None
	"""
	proceed_game = startGame()
	userScore, computerScore = 0, 0
	playerScores = {'Computer': 0,'Player': 0}			
	items = ['rock','paper','scissors']
	no_of_rounds = 1
	if proceed_game == 'Y' or proceed_game == 'YES':
		print('\nHey player! welcome to single player mode 🎮')
		print('\nIn this mode, you battle with the computer for as many rounds as possible.')
		print('\nAfter each round, the winner earns a point.')
		print('\nThe first player to reach 7 points wins the game 🚀🚀')
		print('\nGoodluck!')
		print('\nEnter exit to end game')
		print('\nIf you exit the game, the computer wins the game by default\n')
		while True:
			if userScore == 7:
				print('\nGame over!!\n')
				print('\nPlayers \t\t    Points')	
				print('-' * 35)
				print('{}\t\t\t    {}pts'.format('You'.capitalize(), userScore))
				print('{}\t\t    {}pts'.format('Computer', computerScore))	
				print('\nCongratulations, you\'ve won the game 🚀🚀\n')	
				break
			if computerScore == 7:
				print('\nGame over!!\n')	
				print('\nPlayers \t\t    Points')	
				print('-' * 35)
				print('{}\t\t    {}pts'.format('Computer', computerScore))	
				print('{}\t\t\t    {}pts'.format('You'.capitalize(), userScore))
				print('\nComputer won the game!..try harder next time 😉\n')	
				break
			else:	
				#generate a random number and assign it to a variable n	
				#this determines the computer's choice
				n = random.randint(1,3)
				if n == 1: computer_choice = 'rock'
				if n == 2: computer_choice = 'paper'
				if n == 3: computer_choice = 'scissors'
				print(f'\n\tRound {no_of_rounds}')
				player_choice = input('\nEnter your choice (rock/paper/scissors): ')
				player_choice = player_choice.strip().lower()
				while player_choice not in items and player_choice != 'exit':
					print('Invalid input!')
					player_choice = input('\nEnter a valid choice (rock/paper/scissors): ')
					player_choice = player_choice.strip().lower()	
				if player_choice == 'exit':
					exit_game = exitGame()
					if exit_game == 'YES' or exit_game == 'Y':
						print('\nYou exited the game, Computer wins the game by default 🚀🚀')
						break
					else: player_choice != 'exit'			
				if player_choice != 'exit':
					print('\nYou selected {}'.format(player_choice))
					print('Computer selected {}'.format(computer_choice))
					if player_choice == 'rock':
						if computer_choice == 'paper':
							computerScore += 1
							playerScores['Computer'] = computerScore
							print('Computer wins!..Computer just earned a point')
						elif computer_choice == 'scissors':
							userScore += 1
							playerScores['Player'] = userScore
							print('You win!...You just earned a point')
						elif computer_choice == 'rock':
							print('No winner!!..play again to determine the winner')
					elif player_choice == 'paper':
						if computer_choice == 'rock':
							userScore += 1
							playerScores['Player'] = userScore
							print('You win!...You just earned a point')
						elif computer_choice == 'scissors':
							computerScore += 1
							playerScores['Computer'] = computerScore
							print('Computer wins!..Computer just earned a point')
						elif computer_choice == 'paper':
							print('No winner!!..play again to determine the winner')
					elif player_choice == 'scissors':
						if computer_choice == 'paper':
							userScore += 1
							playerScores['Player'] = userScore
							print('You win!...You just earned a point')
						elif computer_choice == 'rock':
							computerScore += 1
							playerScores['Computer'] = computerScore
							print('Computer wins!..Computer just earned a point')
						elif computer_choice == 'scissors':
							print('No winner!!..play again to determine the winner')
					no_of_rounds += 1			
	if proceed_game == 'N' or proceed_game == 'NO': 
		print('Bye player!')		