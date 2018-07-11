# this program simulates natural selection

# timeline:
# DONE - generate species, many variations
# DONE - test against certain environments
# DONE - kill those that cannot survive
# those that survive breed
# these offspring will have minor mutations and be tested against new environments

import random
from environment import Environment
from species import Species

# defining environments, all environment variables begin with e

eHarsh = Environment(-5)
eSemiHarsh = Environment(-4)
eModerate = Environment(-3)
eSemiModerate = Environment(-2)
eEasy = Environment(-1)
ePeaceful = Environment(0)
eBeneficial = Environment(1)

environments = [eBeneficial,ePeaceful,eEasy,eSemiModerate,eModerate,eSemiHarsh,eHarsh]

def dataset(amount):
	data = []
	for num in range(0,amount):
		data.append(Species.genRandomSpecies())
	return data

def testAndKill(data,environment):
	for species in data:
		position = 0
		if species.testAgainst(environments[environment]) == False:
			del data[position]
		position += 1

	return data

speciesList = dataset(100000)
print(len(speciesList))

for num in range(0,40):
	speciesList = testAndKill(speciesList,6)
	print(len(speciesList))