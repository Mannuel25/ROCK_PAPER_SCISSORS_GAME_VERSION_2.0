def exitGame():
	"""
	Returns player's response to either exit or continue game
	:return: str
	"""
	exit_game_picks = ['YES','Y','N','NO']	#possible picks to continue or end game
	confirm_exit = input('\nAre you sure you wanna exit?..all progress would be lost (yes/no): ')
	confirm_exit = confirm_exit.strip().upper()
	while confirm_exit not in exit_game_picks :
		print('Invalid input!')
		confirm_exit =input('\nAre you sure you wanna exit?..all progress would be lost (yes/no): ')
		confirm_exit = confirm_exit.strip().upper()
	return confirm_exit
