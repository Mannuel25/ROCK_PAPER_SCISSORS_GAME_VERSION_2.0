import random
from get_player_username import PlayerUsername

def rooms_selection(serverRooms):
	"""
	Returns a list of players room
	:return : list(str)
	"""
	PlayersUsername = PlayerUsername(serverRooms)
	print('\n\nHey players! welcome to multi-player mode 🎮. The battle for the Ultimate Champion 🏆🏆')
	print('\nIn this mode, players are divided into server room(s). Each room is made up of two randomly paired players')
	print('\nFor 6 number of players:')
	print('\n\t+ The players in server room 1 will play first, and the rest would follow')
	print('\n\t+ it is in three phases, for phase 1..')
	print('\n\t+ the players in each server rooms will battle with each other for as many rounds as possible.')
	print('\n\t+ The first player in each server room to reach 5 points, qualifies for phase 2')
	print('\n\t+ then, the qualifiers will battle with each other for as many rounds as possible.')
	print('\n\t+ The first player in each server room to reach 4 points, qualifies for phase 3')
	print('\n\t+ Phase 3; the last phase consists of eleven(11) rounds, after which a player will emerge as the Ultimate champion!!')
	print('\nFor 4 number of players:')
	print('\n\t+ The players in server room 1 will play first and the rest would follow')
	print('\n\t+ it is in two phases, for phase 1..')
	print('\n\t+ players in each server room will battle with each other for as many rounds as possible.')
	print('\n\t+ The first player in each server room to reach 6 points, qualifies for phase 2')
	print('\n\t+ Phase 2; the last phase consists of seven(7) rounds, after which a player will emerge as the Ultimate champion!!')
	print('\nFor 2 number of players:')
	print('\n\t+ it\'s just a phase..both players will battle with each for as many rounds as possible.')
	print('\n\t+ After each round, the winner earns a point. The first player to reach 10 points wins the game!!')
	print('\n\nIf there\'s a tie in any phase, the players will battle with each other for as many rounds as possible.')
	print('\nThe first player to reach 3 points wins the game or qualifies for the next phase!')
	print('\nGoodluck players!')
	print('\nEnter exit to end the game')
	print('\nIf a player exits the game, the other player wins the game or qualifies for the next phase by default\n')
	players = list(serverRooms)
	print('\n', 'Server rooms')
	if len(players) == 2:
		#select and pair the two players into a server room
		room_1 = random.sample(players, 2)
		print('\n\tRoom 1')
		print('-' * 20)
		print('\n', room_1[0],' vs ', room_1[1])
		return room_1
	elif len(players) == 4:
		#select four random players and
		#pair them into server rooms (2 players in each)
		room_1 = random.sample(players, 2)
		for i in room_1:
			players.pop(players.index(i))
		room_2 = random.sample(players, 2)
		combined_rooms = room_1 + room_2	
		print('\n\tRoom 1')
		print('-' * 20)
		print('\n', room_1[0],' vs ', room_1[1] + '\n')
		print('-' * 26)
		print('-' * 26)
		print('\n\tRoom 2')
		print('-' * 20)
		print('\n', room_2[0],' vs ', room_2[1])
		return combined_rooms
	elif len(players) == 6:
		#select six random players and
		#pair them into server rooms (2 players in each)
		room_1 = random.sample(players, 2)
		for i in room_1:
			players.pop(players.index(i))
		room_2 = random.sample(players, 2)	
		for i in room_2:
			players.pop(players.index(i))
		room_3 = random.sample(players, 2)	
		combined_rooms = room_1 + room_2 + room_3
		print('\n\tRoom 1')
		print('-' * 20)
		print('\n', room_1[0],' vs ', room_1[1] + '\n')
		print('-' * 26)
		print('-' * 26)
		print('\n\tRoom 2')
		print('-' * 20)
		print('\n', room_2[0],' vs ', room_2[1] + '\n')
		print('-' * 26)
		print('-' * 26)
		print('\n\tRoom 3')
		print('-' * 20)
		print('\n', room_3[0],' vs ', room_3[1])
		return combined_rooms