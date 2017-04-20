from recommender.similarItem import *

def item_based(preference_space,person_to_recommend,number_of_item,similarity):
	"""
	Initializing item-based recommender algorithm
		Parameters
	--------------
	preference_space: dictionary type, keys are users while values are dictionary of items and ratings
					ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
										  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
										   .....
										  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
												}
	recommender : 'user_based'  or 'item_based'
	
	number_of_items_to_recommend : integer
	
	similarity : 'euclidean_distance' , 'cosine' or 'pearson_correlation'
	
	Returns
	--------------	
	return list item recommended 
	
	"""


	list_of_my_movie=preference_space[person_to_recommend]
	similarity_table=find_similar_item.find_similar_item(preference_space,number_of_item,similarity)
	rating_time_sim={}
	similarity_sum={}
	
	for (item,rating) in list_of_my_movie.items(): 
		for (similarity_score,similar_item) in similarity_table[item]:
			rating_time_sim.setdefault(similar_item,0)
			rating_time_sim[similar_item]+= similarity_score*rating
			
			similarity_sum.setdefault(similar_item,0)			
			similarity_sum[similar_item]+=similarity_score
							
	results=[(rating_time_sims/similarity_sum[x],x) for x,rating_time_sims in rating_time_sim.items()] 
	
	results.sort()
	results.reverse()
	return [x[1] for x in results[0:number_of_item]	]

	
	


	
	
	
	
