
import user_match, preference_space_transform
from recommender.similarity_measure import *

def find_similar_item(preference_space,n=10,similarity=euclidean_distance):
	"""
	The function return list of similar item for each item in preference space
	The function transform the preference space before checking each item
	Parameters
	--------------
	preference_space: dictionary type, keys are users while values are dictionary of items and ratings
					ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
										  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
										   .....
										  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
												}
	recommender : 'user_based' (default) or 'item_based'
	
	number_of_items_to_recommend: integer(default=10)
	
	similarity : 'euclidean_distance' (default), 'cosine' or 'pearson_correlation'
	
	Returns
	--------------	
    list

	"""
	results={}
	transformed_preference_space=preferance_space_transform(preference_space)
	for item in transformed_preference_space:
		results[item]=user_match(transformed_preference_space,item,n,similarity)			
	return results[0]
