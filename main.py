from black_board import blackboard
from SinglePlayer import singlePlayer
from tiePhase import tie_phase

def main():
	"""
	Controls the entire game
	:return: None
	"""
	serverRooms = {}	#keeps track of player's username and score
	QUIT = 3
	player_blackboard_choice = ''
	while player_blackboard_choice != QUIT:
		player_blackboard_choice = blackboard()
		if player_blackboard_choice == 1: 
			singlePlayer()
		elif player_blackboard_choice == 2: 
			tie_phase(serverRooms)
		
main()			
