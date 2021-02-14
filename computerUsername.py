import random

def computer_username():
	"""
	Returns a random username for the computer
	:return : str
	"""
	#possible username the computer can have
	usernames = ['bella_123','$lade(99)','BADOO_0!','V1rus**',		
		'Gh0stO_O', '1ce_man','MoneyBa9$','1ucy=_=', 'F1ash~_~',
		'<an9el>','-NeGaT1Ve-', '__M4dCat__','|Re$pEcT0|','-D1ggerR-',
		'k^T3st','n1ce!™']
	random.SystemRandom().shuffle(usernames)	
	select_username = ''.join(random.sample(usernames, 1))	#select a random username
	return select_username

