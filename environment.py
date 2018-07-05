import random
import species

# two parts
# 1. the environment
# 2. the testAgainst(species,environment) function

class Environment:
	def __init__(self,difficulty,modifier):
		self.difficulty = difficulty
		self.modifier = modifier