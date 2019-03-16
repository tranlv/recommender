import sys

ALGORITHMS = ['user_based', 'item_based']
SIMILARITIES = ['euclidean_distance','cosine','pearson_correlation']

def make_recomendation(person_to_recommend,
					   preference_space,
					   recommender_approach='user_based',
			 		   number_of_items_to_recommend=10, 
			 		   similarity_measure='euclidean_distance'):

	"""	 Return list of recommendation items

	Parameters
	--------------
	
		person_to_recommend (str): user id/name to recommend to

		preference_space (dict):  keys are user Id's and values are dictionary of items and ratings
						ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
											  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
											   .....
											  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
												}

		recommender_approach (str): support 'user_based' (default) or 'item_based'

		number_of_items_to_recommend (int): number of items to recommend (default=10)

		similarity_measure (str): similarity measurement method , support 'euclidean_distance' (default), 'cosine' or 'pearson_correlation'

	Returns
	--------------	

		list
	"""

	if number_of_items_to_recommend == 0:
		return []

	try:
		isinstance(preference_space, dict)
	except ValueError:
		print("preference space is not dictionary type!")

	try: 
		index = ALGORITHMS.index(recommender_approach)
	except ValueError:
		print("{} is not one of accepted recommender engine, using user-based by default!".format(recommender_approach))
		recommender = user_based
	else:
		recommender = getattr(sys.modules[__name__], recommender_approach)
	
	try: 
		SIMILARITIES.index(similarity_measure)
	except ValueError:
		print("{} is not one of accepted similarity measure, using euclidean_distance by default!".format(similarity_measure))
		similarity_measure = 'euclidean_distance'

	
	return recommender(person_to_recommend=person_to_recommend, \
						preference_space=preference_space, \
			 		   number_of_items_to_recommend=number_of_items_to_recommend, \
			 		   similarity_measure=similarity_measure) 


def item_based(person_to_recommend, preference_space, number_of_items_to_recommend=10, similarity_measure='euclidean_distance'):

	""" return list of recommended items using item_based approach
	
	Parameters
	--------------
		person_to_recommend (str): user id/name that we need to recommend to

		preference_space (dict):  keys are user Id's and values are dictionary of items and ratings
						ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
											  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
											   .....
											  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
													}

		number_of_items_to_recommend (int): number of items to recommend (default=10)

		similarity_measure (str): similarity measurement method , support 'euclidean_distance' (default), 'cosine' or 'pearson_correlation'

	Returns
	--------------	

		list
	
	"""


	list_of_items = preference_space[person_to_recommend]
	from .similar_item.find_similar_item import find_similar_item
	similarity_table = find_similar_item(preference_space, number_of_items_to_recommend, similarity_measure)
	rating_time_sim = {}
	similarity_sum = {}
	
	for (item,rating) in list_of_items.items(): 
		for (similarity_score,similar_item) in similarity_table[item]:
			rating_time_sim.setdefault(similar_item, 0)
			rating_time_sim[similar_item]+= similarity_score*rating
			
			similarity_sum.setdefault(similar_item, 0)			
			similarity_sum[similar_item]+=similarity_score
							
	results=[(rating_time_sims/similarity_sum[x], x) for x,rating_time_sims in rating_time_sim.items()] 
	
	results.sort()
	results.reverse()
	return [x[1] for x in results[0:number_of_items_to_recommend]]

def user_based(person_to_recommend, preference_space, number_of_items_to_recommend=10, similarity_measure='euclidean_distance'):

	""" return list of recommended items using user_based approach
	
	Parameters
	--------------
		person_to_recommend (str): user id/name that we need to recommend to

		preference_space (dict):  keys are user Id's and values are dictionary of items and ratings
						ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
											  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
											   .....
											  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
													}

		number_of_items_to_recommend (int): number of items to recommend (default=10)

		similarity_measure (str): similarity measurement method , support 'euclidean_distance' (default), 'cosine' or 'pearson_correlation'

	Returns
	--------------	

		list
	
	"""

	totals={}
	similarity_sum={}

	for other_person in preference_space:	
		if other_person == person_to_recommend: 
			continue
		from importlib import import_module
		sim_mod= import_module("recommender.similarity_measure."  + similarity_measure)
		sim_func = getattr(sim_mod, similarity_measure)
		sim = sim_func(preference_space, person_to_recommend, other_person)		
		
		if sim <= 0: 
			continue	

		for item in preference_space[other_person] :
			if item not in preference_space[person_to_recommend] or preference_space[person_to_recommend][item]==0:
				totals.setdefault(item,0) #if item not in dict, will set default to 0
				totals[item] += sim * preference_space[other_person][item]
				similarity_sum.setdefault(item,0)
				similarity_sum[item] += sim		

	results=[(totals[item] / similarity_sum[item],item) for item in totals.keys()]
	results.sort()
	results.reverse()

	return [x[1] for x in results[0:number_of_items_to_recommend]]
	
	


	

