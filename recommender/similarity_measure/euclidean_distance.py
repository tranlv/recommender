"""
	return euclidean distance measure @ https://en.wikipedia.org/wiki/Euclidean_distance
	Preference_space is a dictionary , keys are users, values are dictionary of items and ratings 
"""
					
from math import pow	
				
def euclidean_distance(preference_space, person1, person2):
	number = 0
	for item in preference_space[person1]:
		if item in preference_space[person2]:
			number= number+ 1
		else: continue
			
	if number == 0:
		return 0 
		
	sum_of_square= sum([pow(preference_space[person1][item]-preference_space[person2][item],2) 
					for item in preference_space[person1] if item in preference_space[person2]])
	
	return 1/(1+sum_of_square)	
