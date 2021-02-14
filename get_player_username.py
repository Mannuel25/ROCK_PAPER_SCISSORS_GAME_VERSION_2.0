import string
from number_of_players import numberOfPlayers

def PlayerUsername(serverRooms):
	"""
	Gets each player's username 
	:return : None
	"""
	no_of_players = numberOfPlayers()
	print('\nEnter a valid username that conforms to the following rules:')
	print('\t+ Minimum length is 5')
	print('\t+ Maximum length is 10')
	print('\t+ Should contain at least a number')
	print('\t+ Should contain at least a special character (such as $,_,+,-,!,*,^,&,@,#,etc)')
	print('\t+ Should contain at least a lowercase or a uppercase letter')
	print('\t+ Should not contain space(s)')
	for i in range(1, no_of_players + 1):
		player_username = input(F'\nPlayer {i}, enter a valid username: ')
		player_username = player_username.strip()
		while not(5 <= len(player_username) <= 10):
			print('Invalid username!')
			player_username = input(F'\nPlayer {i}, enter a valid username: ')
		while ' ' in player_username:
			print('Invalid username!')
			player_username = input(F'\nPlayer {i}, enter a valid username: ')
		while not any(i in string.punctuation for i in player_username):
			print('Invalid username!')
			player_username = input(F'\nPlayer {i}, enter a valid username: ')
		while not any(i in string.digits for i in player_username):
			print('Invalid username!')
			player_username = input(F'\nPlayer {i}, enter a valid username: ')
		while not any(i in string.ascii_letters for i in player_username):
			print('Invalid username!')
			player_username = input(F'\nPlayer {i}, enter a valid username: ')
		while player_username in serverRooms:
			print('oops..username has been taken')
			player_username = input(F'\nPlayer {i}, enter a valid username: ')	
		else:	
			print('Valid username..your username has been saved!')
			serverRooms[player_username] = 0	#initial player score is zero