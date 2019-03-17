from math import sqrt

def cosine(preference_space, person1, person2):
""" return cosine similarity measure @ https://en.wikipedia.org/wiki/Cosine_similarity
	
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

	common_interest=[x for x in preference_space[person1] if x in preference[person2]]
	vector1=map(lambda x: 1 if x in common_interest else 0, preference_space[person1])
	vector2=map(lambda x: 1 if x in common_interest else 0, preference_space[person2])
	square_vector1=[x*x for x in vector1]
	square_vector2=[x*x for x in vector2]
	numerator=[x*y for x, y in [vector1, vector2]]
	denominator=sqrt(square_vector1 * square_vector2)
	
	return numerator/denominator