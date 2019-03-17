				
from math import pow	
				
def euclidean_distance(preference_space, person1, person2):
	""" return euclidean distance measure @ https://en.wikipedia.org/wiki/Euclidean_distance
		Parameters
		--------------
			preference_space (dict) keys are users while values are dictionary of items and ratings
							ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
												  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
												   .....
												  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
														}

			person1 (str): user id/name
			
			person2 (str): user id/name
		
		Returns
		--------------	
	    	float
	"""
	

	number = 0
	for item in preference_space[person1]:
		if item in preference_space[person2]:
			number = number+ 1
		else:
			continue
			
	if number == 0:
		return 0 
		
	sum_of_square = sum([pow(preference_space[person1][item]-preference_space[person2][item],2) 
					for item in preference_space[person1] if item in preference_space[person2]])
	
	return 1/(1+sum_of_square)	
