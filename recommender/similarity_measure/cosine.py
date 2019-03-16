"""
	return cosine similarity measure @ https://en.wikipedia.org/wiki/Cosine_similarity
	Preference_space is a dictionary , keys are users, values are dictionary of items and ratings 
"""

from math import sqrt

def cosine(preference_space, person1, person2):
	common_interest=[x for x in preference_space[person1] if x in preference[person2]]
	vector1=map(lambda x: 1 if x in common_interest else 0, preference_space[person1])
	vector2=map(lambda x: 1 if x in common_interest else 0, preference_space[person2])
	square_vector1=[x*x for x in vector1]
	square_vector2=[x*x for x in vector2]
	numerator=[x*y for x, y in [vector1, vector2]]
	denominator=sqrt(square_vector1 * square_vector2)
	
	return numerator/denominator