def blackboard():
	"""
	Returns player's game mode choice
	:return: int
	"""
	print('\n\tBlackboard\n')
	print('1. Single player')
	print('2. Multi player')
	print('3. Quit game')
	BlackboardChoices = [1,2,3]  #possible blackboard choices a player can enter
	try:
		user_choice = int(input('\nSelect an option from the blackboard: '))
	except ValueError:
		print('Invalid input!!')
	else:
		return user_choice if user_choice in BlackboardChoices else print('Invalid input!!') 						
