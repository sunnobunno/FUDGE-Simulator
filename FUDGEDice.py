#Imports
import random

class FDice:
	
	def Roll(self):
		die1 = random.randrange(-1, 2, 1)
		die2 = random.randrange(-1, 2, 1)
		die3 = random.randrange(-1, 2, 1)
		
		total_roll = die1 + die2 + die3
		return total_roll
		