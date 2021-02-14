def numberOfPlayers():
	"""
	Returns the number of players to play game
	:return : int
	""" 
	print('\nEnter the number of players to play (e.g 2,4,6)')
	print('The minimum number of players that can play is 2')
	print('The maximum number of players that can play is 6')
	NumberOfPlayers = ['2', '4', '6']	#number of players that can play game	
	no_of_players = input('\nEnter a valid number of players to play: ')
	no_of_players = no_of_players.strip()
	while no_of_players not in NumberOfPlayers:
		print('Invalid input!')
		no_of_players = input('\nEnter a valid number of players to play (e.g 2,4,6): ')
		no_of_players = no_of_players.strip()
	return int(no_of_players)	
