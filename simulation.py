# this program simulates natural selection

# timeline:
# DONE - generate species, many variations
# DONE - test against certain environments
# kill those that cannot survive
# those that survive breed
# these offspring will have minor mutations and be tested against new environments

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

