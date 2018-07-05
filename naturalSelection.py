# this program simulates natural selection

# timeline:
# DONE - generate species, many variations
# test against certain environments
# kill those that cannot survive
# those that survive breed
# these offspring will have minor mutations and be tested against new environments

import random
import time

class Species:
	def __init__(self,agility,intimidation,strength,aggressiveness,fly,swim,endurance,intelligence,camoflague,size):
		self.agility =  agility
		self.intimidation = intimidation
		self.strength = strength
		self.aggressiveness = aggressiveness
		self.fly = fly
		self.swim = swim
		self.endurance = endurance
		self.intelligence = intelligence
		self.camoflague = camoflague
		self.size = size

		self.stats = {
			'Agility': agility,
			'Intimidation': intimidation,
			'Strength': strength,
			'Aggressiveness': aggressiveness,
			'Fly': fly,
			'Swim': swim,
			'Endurance': endurance,
			'Intelligence': intelligence,
			'Camoflague': camoflague,
			'Size': size					
			}

		# the name is defined as the highest value above

		self.name = max(self.stats, key=self.stats.get)


	def __str__(self):
		return "Name: %s\nAgility: %f\nIntimidation: %f\nStrength: %f\nAggressiveness: %f\nFly: %r\nSwim: %r\nEndurance: %f\nIntelligence: %f\nCamoflague: %f\nSize: %f" % (self.name, self.agility, self.intimidation, self.strength, self.aggressiveness, bool(self.fly), bool(self.swim), self.endurance, self.intelligence, self.camoflague, self.size)

speciesList = []

def genRandomSpecies(amount):
	for num in range(0,amount):
		speciesList.append(Species(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),0.1,0.1,random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))

	return ''

def getAvgStat(stat):
	total = 0
	amount = 0
	for entry in speciesList:
		total += entry.stats.get(stat)
		amount += 1
		
	average = total / amount
	
	return average

class Environment:
	def __init__(self,difficulty,modifier):
		self.difficulty = difficulty
		self.modifier = modifier

if __name__ == '__main__':

	testSpecies = Species(0.24,0.45,0.3,0.12,.1,.1,0.89,0.46,0.26,0.33)
	# all max values

	genRandomSpecies(3)

	for data in speciesList:
		print(data)
		print('\n')
	
	print(getAvgStat('Endurance'))