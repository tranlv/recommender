
from recommender.similarityMeasure import *

def user_based(preference_space,person_to_recommend,number_of_items,similarity):
	"""
	Initializing user-based recommender algorithm
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
	return list of items recommended 
	
	"""


	totals={}
	similarity_sum={}
	for other_person in preference_space:	
		if other_person==person_to_recommend: continue
		sim=similarity(preference_space,person_to_recommend,other_person)		
		
		if sim<=0: continue	

		for item in preference_space[other_person] :
			if item not in preference_space[person_to_recommend] or preference_space[person_to_recommend][item]==0:
				totals.setdefault(item,0) #if item not in dict, will set default to 0
				totals[item]+=sim*preference_space[other_person][item]
				similarity_sum.setdefault(item,0)
				similarity_sum[item]+=sim		
	results=[(total[item]/similarity_sum[item],item) for item in totals.keys()]	
	results.sort()
	results.reverse()
	return [x[1] for x in results[0:number_of_items]]