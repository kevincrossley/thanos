import numpy as np
import random

##     
## MIT License
## Copyright (c) 2019 Kevin Crossley
##


pop = 7500000000 # world population
maxsnaps = 63 # max number of snaps 
printOn=True # whether you want the specific simulation to print out or not

pop_original = pop

## Specific simulations

def snap(pop):
	pop = pop/2
	return np.floor(pop) # assume Thanos kills until he's above 50% dead

def snapSim(pop, maxsnaps, printOn = False):

	if printOn: print('\n', ' ************* ONE SIMULATION ************* ')
	## 1 Simulation
	for s in range(1,maxsnaps+1):
		if pop <= 2: # once snapping again would leave less than 1 human
			
			pop = random.choice([1, 0]) # 50% chance of death each remaining snap
			if printOn: print('Snap:', s, 'Pop:', pop)
			if pop == 0:
				if printOn: print('Nobody made it this time :(')
				break

		else: # as long as there's more than 1 person, keep killing
			pop = snap(pop)
			if printOn: print('Snap:', s, 'Pop:', pop)

	if pop >= 1 and printOn: print('Someone made it this time!')

	return pop, s


## General Case
s2one = np.floor(np.log2(pop)) # snaps until down to 1 population

print('\n',' ************* SETUP ************* ')
print('Initial Population:', pop_original, 'Max Snaps:', maxsnaps)

if maxsnaps > s2one:
	pop, s = snapSim(pop, maxsnaps, printOn)

	# chance of last person surviving is 50% for each remaining snap
	schance = (0.5)**(maxsnaps - s2one)

	print('\n', ' ************* GENERAL SOLUTION ************* ')
	print('Snaps until just 1 person left:', s2one)
	print('Chance of last person surviving the rest of the snaps (%):', schance*100)

else:
	# percentage of population remaining
	pop, s = snapSim(pop, maxsnaps, printOn)
	schance = pop / pop_original

	print('\n', ' ************* GENERAL SOLUTION ************* ')
	print('Percentage of original population remaining (%):', round(schance*100, 10))
	print('Percent chance that nobody survives (%):', round(100*(1-schance), 10))




