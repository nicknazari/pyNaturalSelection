import random
from environment import Environment

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

		# fitness is only to be used in the environment test variable
		self.fitness = agility + intimidation + strength + aggressiveness + endurance + intelligence + camoflague + size + fly / 10 + swim / 10

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

		self.max = max(self.stats, key=self.stats.get)

	def __str__(self):
		return "Max: %s\nAgility: %f\nIntimidation: %f\nStrength: %f\nAggressiveness: %f\nFly: %r\nSwim: %r\nEndurance: %f\nIntelligence: %f\nCamoflague: %f\nSize: %f" % (self.max, self.agility, self.intimidation, self.strength, self.aggressiveness, bool(self.fly), bool(self.swim), self.endurance, self.intelligence, self.camoflague, self.size)

	def genRandomSpecies():
		return Species(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.randint(0,1)/10,random.randint(0,1)/10,random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))

	def getAvgStat(data,stat):
		total = 0
		amount = 0
		for entry in data:
			total += entry.stats.get(stat)
			amount += 1
			
		average = total / amount

		return average


	def testAgainst(self,environment):

		# this ensures that there is variance when the test is done.
		variance_modifier = environment.modifier + random.uniform(-1,1)

		# the result of this determines whether or not the species survives. if negative, the species does not survive
		test = self.fitness + environment.modifier

		if test > 0:
			return True
		if test < 0:
			return False
		

if __name__ == '__main__':

	testSpecies = Species(0.24,0.45,0.3,0.12,.1,0,0.89,0.46,0.26,0.33)
	# all max values

	collection = []

	for num in range(0,100):
		collection.append(Species.genRandomSpecies())

	print(Species.getAvgStat(collection,'Size'))

	harshEnvironment = Environment(-5)

	print('fitness: ' + str(testSpecies.fitness))
	
	print(testSpecies.testAgainst(harshEnvironment))