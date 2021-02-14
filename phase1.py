from start_game import startGame
from players_rooms import rooms_selection

def phase_1(serverRooms):
	"""
	Returns the winner(s) for phase 1
	:return : str
	"""
	start_game = startGame()	
	if start_game == 'YES' or start_game == 'Y':
		serverRooms.clear()			#clear existing server rooms 
		players = rooms_selection(serverRooms)
		print('\n' + '-' * 98)
		print('-' * 98)	
		print('\n\tPhase 1')
		items = ['rock','paper','scissors']
		if len(players) == 2:
			player_1, player_2 = players[0], players[1]
			player_1_score, player_2_score = 0, 0
			no_of_rounds = 1
			#spaces are used to format the printing of the
			#players points table
			spaces_1, spaces_2 = 10 - len(player_1), 10 - len(player_2)	
			player_1 += ' ' * spaces_1
			player_2 += ' ' * spaces_2
			while True:
				if player_1_score == 10:
					print('\nGame over!!\n')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print(f'\nCongratulations {player_1.strip()}, you\'ve won the game 🚀🚀\n')
					for i in range(4):
						print('\n' + '🎈 ' * 40) 
					print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_1.strip()}')
					return player_1
					break
				if player_2_score == 10:
					print('\nGame over!!\n')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print(f'\nCongratulations {player_2.strip()}, you\'ve won the game 🚀🚀\n')
					for i in range(4):
						print('\n' + '🎈 ' * 40) 
					print(f'\nOur Ultimate Champion 🏆🏆 for this game is {player_2.strip()}')
					return player_2
					break
				else:
					print(f'\n\n\tRound {no_of_rounds}')
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
						return player_2
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
						return player_1
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
		elif len(players) == 4:
			cumulate_qualifiers = []
			player_1, player_2 = players[0], players[1]
			player_3, player_4 = players[2], players[3]
			player_1_score, player_2_score = 0, 0
			player_3_score, player_4_score = 0, 0
			room1_no_of_rounds,	room2_no_of_rounds = 1, 1
			room3_no_of_rounds, room4_no_of_rounds= 1, 1
			#spaces are used to format the printing of
			#the players points table
			spaces_1, spaces_2 = 10 - len(player_1), 10 - len(player_2)
			spaces_3, spaces_4 = 10 - len(player_3), 10 - len(player_4)
			player_1 += ' ' * spaces_1
			player_2 += ' ' * spaces_2
			player_3 += ' ' * spaces_3
			player_4 += ' ' * spaces_4
			while player_1_score or player_2_score != 7:
				if player_1_score == 6:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print(F'\nCongratulations {player_1.strip()}, you\'ve qualified for phase 2!')
					break
				if player_2_score == 6:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print(F'\nCongratulations {player_2.strip()}, you\'ve qualified for phase 2!')
					break
				else:	
					print('\n\n\tRoom 1')
					print('-' * 19)
					print(f'\n\tRound {room1_no_of_rounds}')
					player_1_choice = input(f'\nEnter your choice {player_1.strip()} (rock/paper/scissors): ')
					player_1_choice = player_1_choice.strip().lower()
					while player_1_choice not in items and player_1_choice != 'exit':
						print('Invalid input!')
						player_1_choice = input(f'\nEnter a valid choice {player_1.strip()} (rock/paper/scissors): ')
						player_1_choice = player_1_choice.strip().lower()		
					if player_1_choice == 'exit':
						player_2_choice = 'exit'
						serverRooms[f'{player_2.strip()}'] = 6
						print(f'\n{player_1.strip()} exited the game..')
						print(F'\nCongratulations {player_2.strip()}, you\'ve qualified for phase 2 by default')
						break
					if player_1_choice != 'exit':
							player_2_choice = input(f'\nEnter your choice {player_2.strip()} (rock/paper/scissors): ')
							player_2_choice = player_2_choice.strip().lower()				
					while player_2_choice not in items and player_2_choice != 'exit':
						print('Invalid input!')
						player_2_choice = input(f'\nEnter a valid choice {player_2.strip()} (rock/paper/scissors): ')
						player_2_choice = player_2_choice.strip().lower()	
					if player_2_choice == 'exit':
						serverRooms[f'{player_1.strip()}'] = 6
						print(f'\n{player_2.strip()} exited the game..')
						print(F'\nCongratulations {player_1.strip()}, you\'ve qualified for phase 2 by default')
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
						room1_no_of_rounds += 1		
			conditions = [player_1_choice == 'exit', player_2_choice == 'exit',
				player_1_score == 6, player_2_score == 6]			
			while any(conditions):
				if player_3_score == 6:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_3, player_3_score))
					print('{}\t\t \t{}pts'.format(player_4, player_4_score))
					print(F'\nCongratulations {player_3.strip()}, you\'ve qualified for phase 2!')
					break
				if player_4_score == 6:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_4, player_4_score))
					print('{}\t\t \t{}pts'.format(player_3, player_3_score))
					print(F'\nCongratulations {player_4.strip()}, you\'ve qualified for phase 2!')		
					break		
				else:			
					print('\n\n\tRoom 2')
					print('-' * 19)
					print(f'\n\tRound {room2_no_of_rounds}')
					player_3_choice = input(f'\nEnter your choice {player_3.strip()} (rock/paper/scissors): ')
					player_3_choice = player_3_choice.strip().lower()
					while player_3_choice not in items and player_3_choice != 'exit' :
						print('Invalid input!')
						player_3_choice = input(f'\nEnter a valid choice {player_3.strip()} (rock/paper/scissors): ')
						player_3_choice = player_3_choice.strip().lower()		
					if player_3_choice == 'exit':
						serverRooms[f'{player_4.strip()}'] = 6
						print(f'\n{player_3.strip()} exited the game..')
						print(F'\nCongratulations {player_4.strip()}, you\'ve qualified for phase 2 by default')
						break
					if player_3_choice != 'exit':
							player_4_choice = input(f'\nEnter your choice {player_4.strip()} (rock/paper/scissors): ')
							player_4_choice = player_4_choice.strip().lower()				
					while player_4_choice not in items and player_4_choice != 'exit':
						print('Invalid input!')
						player_4_choice = input(f'\nEnter a valid choice {player_4.strip()} (rock/paper/scissors): ')
						player_4_choice = player_4_choice.strip().lower()	
					if player_4_choice == 'exit':
						serverRooms[f'{player_3.strip()}'] = 6
						print(f'\n{player_4.strip()} exited the game..')
						print(F'\nCongratulations {player_3.strip()}, you\'ve qualified for phase 2 by default')
						break		
					if player_3_choice != 'exit' or player_4_choice != 'exit':	
						print('\n{} selected {}'.format(player_3.strip(), player_3_choice))
						print('{} selected {}'.format(player_4.strip(), player_4_choice))
						if player_3_choice == 'rock':
							if player_4_choice == 'paper':
								player_4_score += 1
								serverRooms[f'{player_4.strip()}'] = player_4_score
								print(f'{player_4.strip()} wins!..{player_4.strip()} just earned a point')
							elif player_4_choice == 'scissors':
								player_3_score += 1
								serverRooms[f'{player_3.strip()}'] = player_3_score
								print(f'{player_3.strip()} wins!..{player_3.strip()} just earned a point')
							elif player_3_choice == 'rock':
								print('No winner!!..play again to determine the winner')
						elif player_3_choice == 'paper':
							if player_4_choice == 'rock':
								player_3_score += 1
								serverRooms[f'{player_3.strip()}'] = player_3_score
								print(f'{player_3.strip()} wins!..{player_3.strip()} just earned a point')
							elif player_4_choice == 'scissors':
								player_4_score += 1
								serverRooms[f'{player_4.strip()}'] = player_4_score
								print(f'{player_4.strip()} wins!..{player_4.strip()} just earned a point')
							elif player_4_choice == 'paper':
								print('No winner!!..play again to determine the winner')
						elif player_3_choice == 'scissors':
							if player_4_choice == 'paper':
								player_3_score += 1
								serverRooms[f'{player_3.strip()}'] = player_3_score
								print(f'{player_3.strip()} wins!..{player_3.strip()} just earned a point')
							elif player_4_choice == 'rock':
								player_4_score += 1
								serverRooms[f'{player_4.strip()}'] = player_4_score
								print(f'{player_4.strip()} wins!..{player_4.strip()} just earned a point')
							elif player_4_choice == 'scissors':
								print('No winner!!..play again to determine the winner')
						room2_no_of_rounds += 1			
			print('\nQualifiers for phase 2 🏁 :')				
			for player, score in serverRooms.items():
				if score == 6:
					print(f'\n\t+ {player}') 	
					cumulate_qualifiers.append(player)
			phase_2_qualifiers = ','.join(cumulate_qualifiers)			
			return phase_2_qualifiers			
		elif len(players) == 6:
			cumulate_qualifiers = []
			player_1, player_2 = players[0], players[1]
			player_3, player_4 = players[2], players[3]
			player_5, player_6 = players[4], players[5]
			player_1_score, player_2_score = 0, 0
			player_3_score, player_4_score = 0, 0
			player_5_score, player_6_score = 0, 0
			room1_no_of_rounds,	room2_no_of_rounds = 1, 1
			room3_no_of_rounds = 1
			#spaces are used to format the printing of
			#the players points table 
			spaces_1, spaces_2 = 10 - len(player_1), 10 - len(player_2)
			spaces_3, spaces_4 = 10 - len(player_3), 10 - len(player_4)
			spaces_5, spaces_6 = 10 - len(player_5), 10 - len(player_6)
			player_1 += ' ' * spaces_1
			player_2 += ' ' * spaces_2
			player_3 += ' ' * spaces_3
			player_4 += ' ' * spaces_4
			player_5 += ' ' * spaces_5
			player_6 += ' ' * spaces_6
			while player_1_score or player_2_score != 6:
				if player_1_score == 5:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print(F'\nCongratulations {player_1.strip()}, you\'ve qualified for phase 2!')
					break
				if player_2_score == 5:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_2, player_2_score))
					print('{}\t\t \t{}pts'.format(player_1, player_1_score))
					print(F'\nCongratulations {player_2.strip()}, you\'ve qualified for phase 2!')
					break
				else:	
					print('\n\n\tRoom 1')
					print('-' * 19)		
					print(f'\n\tRound {room1_no_of_rounds}')
					player_1_choice = input(f'\nEnter your choice {player_1.strip()} (rock/paper/scissors): ')
					player_1_choice = player_1_choice.strip().lower()
					while player_1_choice not in items and player_1_choice != 'exit':
						print('Invalid input!')
						player_1_choice = input(f'\nEnter a valid choice {player_1.strip()} (rock/paper/scissors): ')
						player_1_choice = player_1_choice.strip().lower()		
					if player_1_choice == 'exit':
						player_2_choice = 'exit'
						serverRooms[f'{player_2.strip()}'] = 5
						print(f'\n{player_1.strip()} exited the game..')
						print(F'\nCongratulations {player_2.strip()}, you\'ve qualified for phase 2 by default')
						break
					if player_1_choice != 'exit':
							player_2_choice = input(f'\nEnter your choice {player_2.strip()} (rock/paper/scissors): ')
							player_2_choice = player_2_choice.strip().lower()				
					while player_2_choice not in items and player_2_choice != 'exit':
						print('Invalid input!')
						player_2_choice = input(f'\nEnter a valid choice {player_2.strip()} (rock/paper/scissors): ')
						player_2_choice = player_2_choice.strip().lower()	
					if player_2_choice == 'exit':
						serverRooms[f'{player_1.strip()}'] = 5
						print(f'\n{player_2.strip()} exited the game..')
						print(F'\nCongratulations {player_1.strip()}, you\'ve qualified for phase 2 by default')
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
						room1_no_of_rounds += 1		
			condition_1 = [player_1_choice == 'exit', player_2_choice == 'exit',
				player_1_score == 5, player_2_score == 5]			
			while any(condition_1):
				if player_3_score == 5:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_3, player_3_score))
					print('{}\t\t \t{}pts'.format(player_4, player_4_score))
					print(F'\nCongratulations {player_3.strip()}, you\'ve qualified for phase 2!')
					break
				if player_4_score == 5:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_4, player_4_score))
					print('{}\t\t \t{}pts'.format(player_3, player_3_score))	
					print(F'\nCongratulations {player_4.strip()}, you\'ve qualified for phase 2!')	
					break		
				else:			
					print('\n\n\tRoom 2')
					print('-' * 19)
					print(f'\n\tRound {room2_no_of_rounds}')
					player_3_choice = input(f'\nEnter your choice {player_3.strip()} (rock/paper/scissors): ')
					player_3_choice = player_3_choice.strip().lower()
					while player_3_choice not in items and player_3_choice != 'exit' :
						print('Invalid input!')
						player_3_choice = input(f'\nEnter a valid choice {player_3.strip()} (rock/paper/scissors): ')
						player_3_choice = player_3_choice.strip().lower()		
					if player_3_choice == 'exit':
						player_4_choice = 'exit'
						serverRooms[f'{player_4.strip()}'] = 5
						print(f'\n{player_3.strip()} exited the game..')
						print(F'\nCongratulations {player_4.strip()}, you\'ve qualified for phase 2 by default')
						break
					if player_3_choice != 'exit':
							player_4_choice = input(f'\nEnter your choice {player_4.strip()} (rock/paper/scissors): ')
							player_4_choice = player_4_choice.strip().lower()				
					while player_4_choice not in items and player_4_choice != 'exit':
						print('Invalid input!')
						player_4_choice = input(f'\nEnter a valid choice  {player_4.strip()} (rock/paper/scissors): ')
						player_4_choice = player_4_choice.strip().lower()	
					if player_4_choice == 'exit':
						serverRooms[f'{player_3.strip()}'] = 5
						print(f'\n{player_4.strip()} exited the game..')
						print(F'\nCongratulations {player_3.strip()}, you\'ve qualified for phase 2 by default')
						break		
					if player_3_choice != 'exit' or player_4_choice != 'exit':	
						print('\n{} selected {}'.format(player_3.strip(), player_3_choice))
						print('{} selected {}'.format(player_4.strip(), player_4_choice))
						if player_3_choice == 'rock':
							if player_4_choice == 'paper':
								player_4_score += 1
								serverRooms[f'{player_4.strip()}'] = player_4_score
								print(f'{player_4.strip()} wins!..{player_4.strip()} just earned a point')
							elif player_4_choice == 'scissors':
								player_3_score += 1
								serverRooms[f'{player_3.strip()}'] = player_3_score
								print(f'{player_3.strip()} wins!..{player_3.strip()} just earned a point')
							elif player_3_choice == 'rock':
								print('No winner!!..play again to determine the winner')
						elif player_3_choice == 'paper':
							if player_4_choice == 'rock':
								player_3_score += 1
								serverRooms[f'{player_3.strip()}'] = player_3_score
								print(f'{player_3.strip()} wins!..{player_3.strip()} just earned a point')
							elif player_4_choice == 'scissors':
								player_4_score += 1
								serverRooms[f'{player_4.strip()}'] = player_4_score
								print(f'{player_4.strip()} wins!..{player_4.strip()} just earned a point')
							elif player_4_choice == 'paper':
								print('No winner!!..play again to determine the winner')
						elif player_3_choice == 'scissors':
							if player_4_choice == 'paper':
								player_3_score += 1
								serverRooms[f'{player_3.strip()}'] = player_3_score
								print(f'{player_3.strip()} wins!..{player_3.strip()} just earned a point')
							elif player_4_choice == 'rock':
								player_4_score += 1
								serverRooms[f'{player_4.strip()}'] = player_4_score
								print(f'{player_4.strip()} wins!..{player_4.strip()} just earned a point')
							elif player_4_choice == 'scissors':
								print('No winner!!..play again to determine the winner')
						room2_no_of_rounds += 1	
			condition_2 = [player_3_choice == 'exit', player_4_choice == 'exit',
				player_3_score == 5, player_4_score == 5]			
			while any(condition_2):
				if player_5_score == 5:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_5, player_5_score))
					print('{}\t\t \t{}pts'.format(player_6, player_6_score))
					print(F'\nCongratulations {player_5.strip()}, you\'ve qualified for phase 2!')
					break
				if player_6_score == 5:
					print('\nGame over!!')
					print('\nPlayers \t\t    \tPoints')	
					print('-' * 40)
					print('{}\t\t \t{}pts'.format(player_6, player_6_score))
					print('{}\t\t \t{}pts'.format(player_5, player_5_score))		
					print(F'\nCongratulations {player_6.strip()}, you\'ve qualified for phase 2!')
					break		
				else:			
					print('\n\n\tRoom 3')
					print('-' * 19)
					print(f'\n\tRound {room3_no_of_rounds}')
					player_5_choice = input(f'\nEnter your choice {player_5.strip()} (rock/paper/scissors): ')
					player_5_choice = player_5_choice.strip().lower()
					while player_5_choice not in items and player_5_choice != 'exit' :
						print('Invalid input!')
						player_5_choice = input(f'\nEnter a valid choice {player_5.strip()} (rock/paper/scissors): ')
						player_5_choice = player_5_choice.strip().lower()		
					if player_5_choice == 'exit':
						serverRooms[f'{player_6.strip()}'] = 5
						print(f'\n{player_5.strip()} exited the game..')
						print(F'\nCongratulations {player_6.strip()}, you\'ve qualified for phase 2 by default')
						break
					if player_5_choice != 'exit':
							player_6_choice = input(f'\nEnter your choice {player_6.strip()} (rock/paper/scissors): ')
							player_6_choice = player_6_choice.strip().lower()				
					while player_6_choice not in items and player_6_choice != 'exit':
						print('Invalid input!')
						player_6_choice = input(f'\nEnter a valid choice  {player_6.strip()} (rock/paper/scissors): ')
						player_6_choice = player_6_choice.strip().lower()	
					if player_6_choice == 'exit':
						serverRooms[f'{player_5.strip()}'] = 5
						print(f'\n{player_6.strip()} exited the game..')
						print(F'\nCongratulations {player_5.strip()}, you\'ve qualified for phase 2 by default')
						break		
					if player_5_choice != 'exit' or player_6_choice != 'exit':	
						print('\n{} selected {}'.format(player_5.strip(), player_5_choice))
						print('{} selected {}'.format(player_6.strip(), player_6_choice))
						if player_5_choice == 'rock':
							if player_6_choice == 'paper':
								player_6_score += 1
								serverRooms[f'{player_6.strip()}'] = player_6_score
								print(f'{player_6.strip()} wins!..{player_6.strip()} just earned a point')
							elif player_6_choice == 'scissors':
								player_5_score += 1
								serverRooms[f'{player_5.strip()}'] = player_5_score
								print(f'{player_5.strip()} wins!..{player_5.strip()} just earned a point')
							elif player_5_choice == 'rock':
								print('No winner!!..play again to determine the winner')
						elif player_5_choice == 'paper':
							if player_6_choice == 'rock':
								player_5_score += 1
								serverRooms[f'{player_5.strip()}'] = player_5_score
								print(f'{player_5.strip()} wins!..{player_5.strip()} just earned a point')
							elif player_6_choice == 'scissors':
								player_6_score += 1
								serverRooms[f'{player_6.strip()}'] = player_6_score
								print(f'{player_6.strip()} wins!..{player_6.strip()} just earned a point')
							elif player_6_choice == 'paper':
								print('No winner!!..play again to determine the winner')
						elif player_5_choice == 'scissors':
							if player_6_choice == 'paper':
								player_5_score += 1
								serverRooms[f'{player_5.strip()}'] = player_5_score
								print(f'{player_5.strip()} wins!..{player_5.strip()} just earned a point')
							elif player_6_choice == 'rock':
								player_6_score += 1
								serverRooms[f'{player_6.strip()}'] = player_6_score
								print(f'{player_6.strip()} wins!..{player_6.strip()} just earned a point')
							elif player_6_choice == 'scissors':
								print('No winner!!..play again to determine the winner')
						room3_no_of_rounds += 1	
			print('\nQualifiers for phase 2 🏁 :')				
			for player, score in serverRooms.items():
				if score == 5:
					print(f'\n\t+ {player}') 
					cumulate_qualifiers.append(player)
			phase_2_qualifiers = ','.join(cumulate_qualifiers)	
			return phase_2_qualifiers			
	if start_game == 'NO' or start_game == 'N': 
		print('Bye player!')
		return start_game