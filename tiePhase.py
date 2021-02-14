from phase3 import phase_3

def tie_phase(serverRooms):
	"""
	Controls the game play for tie phase
	:return : None
	"""
	players = phase_3(serverRooms).split(',')
	items = ['rock','paper','scissors']
	usernames = ['bella_123','$lade(99)','BADOO_0!','V1rus**',		#possible username the computer can have
		'Gh0stO_O', '1ce_man','MoneyBa9$','1ucy=_=', 'F1ash~_~',
		'<an9el>','-NeGaT1Ve-', '__M4dCat__','|Re$pEcT0|','-D1ggerR-',
		'k^T3st','n1ce!™']
	if len(players) == 2:
		player_1, player_2 = players[0], players[1]
		player_1_score, player_2_score = 0, 0
		no_of_rounds = 1
		#spaces are used to format the printing of
		#the players points table 
		spaces_1, spaces_2 = 10 - len(player_1), 10 - len(player_2)
		player_1 += ' ' * spaces_1
		player_2 += ' ' * spaces_2
		while True:
			#check if player 2 username is among the listed
			#possible username the computer can have
			#if it is, continue the game manually else
			#randomly generate a choice for the computer
			if player_2.strip() not in usernames:		
				if player_1_score == 3:
					print('\nGame over!!\n')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print(f'\nCongratulations {player_1.strip()}, you\'ve won  the game 🚀🚀\n')
					for i in range(4):
						print('\n' + '🎈 ' * 40) 
					print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_1.strip()}')
					break
				if player_2_score == 3:
					print('\nGame over!!\n')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print(f'\nCongratulations {player_2.strip()}, you\'ve won  the game 🚀🚀\n')
					for i in range(4):
						print('\n' + '🎈 ' * 40) 
					print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_2.strip()}')
					break
				else:
					print(f'\n\tRound {no_of_rounds}')
					player_1_choice = input(f'\nEnter your choice {player_1.strip()} (rock/paper/scissors): ')
					player_1_choice = player_1_choice.strip().lower()
					while player_1_choice not in items and player_1_choice != 'exit' :
						print('Invalid input!')
						player_1_choice = input(f'\nEnter a valid choice {player_1.strip()} (rock/paper/scissors): ')
						player_1_choice = player_1_choice.strip().lower()		
					if player_1_choice == 'exit':
						print(f'\n{player_1.strip()} exited the game..')
						print(F'\nCongratulations {player_2.strip()}, you\'ve won the game by default 🚀🚀')
						for i in range(4):
							print('\n' + '🎈 ' * 40) 
						print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_2.strip()}')
						break
					if player_1_choice != 'exit':
							player_2_choice = input(f'\nEnter your choice {player_2.strip()} (rock/paper/scissors): ')
							player_2_choice = player_2_choice.strip().lower()				
					while player_2_choice not in items and player_2_choice != 'exit':
						print('Invalid input!')
						player_2_choice = input(f'\nEnter a valid choice {player_2.strip()} (rock/paper/scissors): ')
						player_2_choice = player_2_choice.strip().lower()	
					if player_2_choice == 'exit':
						print(f'\n{player_2.strip()} exited the game..')
						print(F'\nCongratulations {player_1.strip()}, you\'ve won the game by default 🚀🚀')
						for i in range(4):
							print('\n' + '🎈 ' * 40) 
						print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_1.strip()}')
						break		
					if player_1_choice != 'exit' or player_2_choice != 'exit':	
						print('\n{} selected {}'.format(player_1.strip(), player_1_choice))
						print('{} selected {}'.format(player_2.strip(), player_2_choice))
						if player_1_choice == 'rock':
							if player_2_choice == 'paper':
								player_2_score += 1
								serverRooms[f'{player_2.strip()}'] = player_2_score
								print(f'{player_2.strip()} wins!..{player_2.strip()} just earned a point')
							elif player_2_choice == 'scissors':
								player_1_score += 1
								serverRooms[f'{player_1.strip()}'] = player_1_score
								print(f'{player_1.strip()} wins!..{player_1.strip()} just earned a point')
							elif player_2_choice == 'rock':
								print('No winner!!..play again to determine the winner')
						elif player_1_choice == 'paper':
							if player_2_choice == 'rock':
								player_1_score += 1
								serverRooms[f'{player_1.strip()}'] = player_1_score
								print(f'{player_1.strip()} wins!..{player_1.strip()} just earned a point')
							elif player_2_choice == 'scissors':
								player_2_score += 1
								serverRooms[f'{player_2.strip()}'] = player_2_score
								print(f'{player_2.strip()} wins!..{player_2.strip()} just earned a point')
							elif player_2_choice == 'paper':
								print('No winner!!..play again to determine the winner')
						elif player_1_choice == 'scissors':
							if player_2_choice == 'paper':
								player_1_score += 1
								serverRooms[f'{player_1.strip()}'] = player_1_score
								print(f'{player_1.strip()} wins!..{player_1.strip()} just earned a point')
							elif player_2_choice == 'rock':
								player_2_score += 1
								serverRooms[f'{player_2.strip()}'] = player_2_score
								print(f'{player_2.strip()} wins!..{player_2.strip()} just earned a point')
							elif player_2_choice == 'scissors':
								print('No winner!!..play again to determine the winner')
						no_of_rounds += 1	
			elif player_2.strip() in usernames:		
				if player_1_score == 3:
					print('\nGame over!!\n')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print(f'\nCongratulations {player_1.strip()}, you\'ve won  the game 🚀🚀\n')
					for i in range(4):
						print('\n' + '🎈 ' * 40) 
					print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_1.strip()}')
					break
				if player_2_score == 3:
					print('\nGame over!!\n')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print(f'\nCongratulations {player_2.strip()}, you\'ve won  the game 🚀🚀\n')
					for i in range(4):
						print('\n' + '🎈 ' * 40) 
					print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_2.strip()}')
					break
				else:
					print(f'\n\tRound {no_of_rounds}')
					player_1_choice = input(f'\nEnter your choice {player_1.strip()} (rock/paper/scissors): ')
					player_1_choice = player_1_choice.strip().lower()
					while player_1_choice not in items and player_1_choice != 'exit' :
						print('Invalid input!')
						player_1_choice = input(f'\nEnter a valid choice {player_1.strip()} (rock/paper/scissors): ')
						player_1_choice = player_1_choice.strip().lower()		
					if player_1_choice == 'exit':
						print(f'\n{player_1.strip()} exited the game..')
						print(F'\nCongratulations {player_2.strip()}, you\'ve won the game by default 🚀🚀')
						for i in range(4):
							print('\n' + '🎈 ' * 40) 
						print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_2.strip()}')
						break
					if player_1_choice != 'exit':
						#generate a random number and assign it to a variable n	
						#this determines player 2's choice
						n = random.randint(1,3)
						if n == 1: player_2_choice = 'rock'
						if n == 2: player_2_choice = 'paper'
						if n == 3: player_2_choice = 'scissors'
					if player_1_choice != 'exit' or player_2_choice != 'exit':	
						print('\n{} selected {}'.format(player_1.strip(), player_1_choice))
						print('{} selected {}'.format(player_2.strip(), player_2_choice))
						if player_1_choice == 'rock':
							if player_2_choice == 'paper':
								player_2_score += 1
								serverRooms[f'{player_2.strip()}'] = player_2_score
								print(f'{player_2.strip()} wins!..{player_2.strip()} just earned a point')
							elif player_2_choice == 'scissors':
								player_1_score += 1
								serverRooms[f'{player_1.strip()}'] = player_1_score
								print(f'{player_1.strip()} wins!..{player_1.strip()} just earned a point')
							elif player_2_choice == 'rock':
								print('No winner!!..play again to determine the winner')
						elif player_1_choice == 'paper':
							if player_2_choice == 'rock':
								player_1_score += 1
								serverRooms[f'{player_1.strip()}'] = player_1_score
								print(f'{player_1.strip()} wins!..{player_1.strip()} just earned a point')
							elif player_2_choice == 'scissors':
								player_2_score += 1
								serverRooms[f'{player_2.strip()}'] = player_2_score
								print(f'{player_2.strip()} wins!..{player_2.strip()} just earned a point')
							elif player_2_choice == 'paper':
								print('No winner!!..play again to determine the winner')
						elif player_1_choice == 'scissors':
							if player_2_choice == 'paper':
								player_1_score += 1
								serverRooms[f'{player_1.strip()}'] = player_1_score
								print(f'{player_1.strip()} wins!..{player_1.strip()} just earned a point')
							elif player_2_choice == 'rock':
								player_2_score += 1
								serverRooms[f'{player_2.strip()}'] = player_2_score
								print(f'{player_2.strip()} wins!..{player_2.strip()} just earned a point')
							elif player_2_choice == 'scissors':
								print('No winner!!..play again to determine the winner')
						no_of_rounds += 1		
