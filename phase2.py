from phase1 import phase_1
from computerUsername import computer_username
import random

def phase_2(serverRooms):
	"""
	Returns the winner(s) for phase 2
	:return: str
	"""
	get_qualifiers = phase_1(serverRooms)
	qualifiers = get_qualifiers.split(',')
	if len(qualifiers) == 1 : return get_qualifiers
	elif len(qualifiers) == 2:
		print('\n' + '-' * 98)
		print('-' * 98)	
		print('\n\tPhase 2')
		items = ['rock','paper','scissors']
		player_1, player_2 = qualifiers[0], qualifiers[1]
		player_1_score, player_2_score = 0, 0
		no_of_rounds = 1
		spaces_1, spaces_2 = 10 - len(player_1), 10 - len(player_2)
		player_1 += ' ' * spaces_1
		player_2 += ' ' * spaces_2
		while True:
			if (player_1_score > player_2_score) and no_of_rounds == 8:
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
			if (player_2_score > player_1_score) and no_of_rounds == 8:
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
			if (player_2_score == player_1_score) and no_of_rounds == 8:
				tie_players = player_1 + ',' + player_2
				print('\nPlayers \t\t    \tPoints')	
				print('-' * 40)
				print('{}\t\t \t{}pts'.format(player_2, player_2_score))
				print('{}\t\t \t{}pts\n'.format(player_1, player_1_score))
				print('\nIt\'s a tie, no winner..')
				print('\nYou\'ll both battle with each other for as many rounds as possible. The first player to reach 3pts wins the game!')
				return tie_players
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
	elif len(qualifiers) == 3:
		print('\n' + '-' * 98)
		print('-' * 98)	
		print('\n\tPhase 2')
		cumulate_qualifiers = []
		items = ['rock','paper','scissors']
		#select four random players and
		#pair them into server rooms (2 players in each)
		room_1 = random.sample(qualifiers, 1)
		for i in room_1:
			qualifiers.pop(qualifiers.index(i))
		#the computer would be added as a player (player 2)
		#generate a random player username for player 2		
		room_1.append(computer_username())		
		room_2 = random.sample(qualifiers, 2)
		combined_rooms = room_1 + room_2	
		print('\n', 'Server rooms')
		print('\n\tRoom 1')
		print('-' * 20)
		print('\n', room_1[0],' vs ', room_1[1] + '\n')
		print('-' * 26)
		print('-' * 26)
		print('\n\tRoom 2')
		print('-' * 20)
		print('\n', room_2[0],' vs ', room_2[1])
		player_1, player_2 = room_1[0], room_1[1]
		player_3, player_4 = room_2[0], room_2[1]
		player_1_score, player_2_score = 0, 0
		player_3_score, player_4_score = 0, 0
		room1_no_of_rounds,	room2_no_of_rounds = 1, 1
		#spaces are used to format the printing of
		#the players points table
		spaces_1, spaces_2 = 10 - len(player_1), 10 - len(player_2)
		spaces_3, spaces_4 = 10 - len(player_3), 10 - len(player_4)
		player_1 += ' ' * spaces_1
		player_2 += ' ' * spaces_2
		player_3 += ' ' * spaces_3
		player_4 += ' ' * spaces_4
		while player_1_score or player_2_score != 5:
			if player_1_score == 4:
				print('\nGame over!!')
				print('\nPlayers \t\t    \tPoints')	
				print('-' * 40)
				print('{}\t\t \t{}pts'.format(player_1, player_1_score))
				print('{}\t\t \t{}pts'.format(player_2, player_2_score))
				print(F'\nCongratulations {player_1.strip()}, you\'ve qualified for phase 3!')
				break
			if player_2_score == 4:
				print('\nGame over!!')
				print('\nPlayers \t\t    \tPoints')	
				print('-' * 40)
				print('{}\t\t \t{}pts'.format(player_2, player_2_score))
				print('{}\t\t \t{}pts'.format(player_1, player_1_score))
				print(F'\nCongratulations {player_2.strip()}, you\'ve qualified for phase 3!')
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
					serverRooms[f'{player_2.strip()}'] = 4
					print(f'\n{player_1.strip()} exited the game..')
					print(F'\nCongratulations {player_2.strip()}, you\'ve qualified for phase 3 by default')
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
					room1_no_of_rounds += 1		
		conditions = [player_1_choice == 'exit', player_2_choice == 'exit',
			player_1_score == 4, player_2_score == 4]			
		while any(conditions):
			if player_3_score == 4:
				print('\nGame over!!')
				print('\nPlayers \t\t    \tPoints')	
				print('-' * 40)
				print('{}\t\t \t{}pts'.format(player_3, player_3_score))
				print('{}\t\t \t{}pts'.format(player_4, player_4_score))
				print(F'\nCongratulations {player_3.strip()}, you\'ve qualified for phase 3!')
				break
			if player_4_score == 4:
				print('\nGame over!!')
				print('\nPlayers \t\t    \tPoints')	
				print('-' * 40)
				print('{}\t\t \t{}pts'.format(player_4, player_4_score))
				print('{}\t\t \t{}pts'.format(player_3, player_3_score))
				print(F'\nCongratulations {player_4.strip()}, you\'ve qualified for phase 3!')		
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
					serverRooms[f'{player_4.strip()}'] = 4
					print(f'\n{player_3.strip()} exited the game..')
					print(F'\nCongratulations {player_4.strip()}, you\'ve qualified for phase 3 by default')
					break
				if player_3_choice != 'exit':
						player_4_choice = input(f'\nEnter your choice {player_4.strip()} (rock/paper/scissors): ')
						player_4_choice = player_4_choice.strip().lower()				
				while player_4_choice not in items and player_4_choice != 'exit':
					print('Invalid input!')
					player_4_choice = input(f'\nEnter a valid choice {player_4.strip()} (rock/paper/scissors): ')
					player_4_choice = player_4_choice.strip().lower()	
				if player_4_choice == 'exit':
					serverRooms[f'{player_3.strip()}'] = 4
					print(f'\n{player_4.strip()} exited the game..')
					print(F'\nCongratulations {player_3.strip()}, you\'ve qualified for phase 3 by default')
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
		print('\nQualifiers for phase 3 🏁 :')				
		for player, score in serverRooms.items():
			if player in combined_rooms and score == 4:
				print(f'\n\t+ {player}') 	
				cumulate_qualifiers.append(player)
		phase_3_qualifiers = ','.join(cumulate_qualifiers) + ','
		return phase_3_qualifiers			
