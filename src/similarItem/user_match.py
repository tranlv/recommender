"""
	The function re turn list of user that match given person 
	The default similarity measure is euclidean distance
"""

from recommender.similarityMeasure import *

def user_match(preference_space,person_to_recommend,n=10,similarity=euclidean_distance):
	result=[(similarity(preference_space,person_to_recommend,other),other) 
			for other in preference_space if other!=person_to_recommend]
	return result[0:n+1]

		