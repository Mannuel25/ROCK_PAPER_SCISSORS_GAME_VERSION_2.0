def startGame():
	"""
	Returns player's response to either start or end game
	:return: str
	"""
	start_or_end_game = ['YES','Y','N','NO']	#possible picks to start or end game
	play_game = input('\nStart game? (yes/no): ')
	play_game = play_game.strip().upper()
	while play_game not in start_or_end_game:
		print('Invalid input!')
		play_game = input('\nStart game? (yes/no): ')
		play_game = play_game.strip().upper()
	return play_game