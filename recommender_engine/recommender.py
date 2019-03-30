#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	make_recommendation - main function to perform recommendation
	item_based and user_based are 2 functions to perform recommendation basen on given approach
 """
from __future__ import print_function, division
import sys
from .similar_item import find_similar_item

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"

ALGORITHMS = ['user_based', 'item_based']
SIMILARITIES = ['euclidean_distance','cosine','pearson_correlation']

def make_recommendation(person_to_recommend,
					   preference_space,
					   recommender_approach='user_based',
			 		   number_of_items_to_recommend=10, 
			 		   similarity_measure='euclidean_distance'):

	"""	 Return list of recommendation items

	Args
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
		return

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

	
	recommendation = recommender(person_to_recommend=person_to_recommend, \
						preference_space=preference_space, \
			 		   number_of_items_to_recommend=number_of_items_to_recommend, \
			 		   similarity_measure=similarity_measure)

	return recommendation

def item_based(person_to_recommend, preference_space, number_of_items_to_recommend=10, similarity_measure='euclidean_distance'):

	""" return list of recommended items using item_based approach
	
	Args
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
	similarity_table = find_similar_item(preference_space, number_of_items_to_recommend, similarity_measure)
	rating_time_sim = {}
	similarity_sum = {}

	for (item, rating) in list_of_items.items():

		for (similarity_score, similar_item) in similarity_table[item]:

			rating_time_sim.setdefault(similar_item, 0)
			rating_time_sim[similar_item] += similarity_score * rating

			similarity_sum.setdefault(similar_item, 0)	
			similarity_sum[similar_item] += similarity_score

	return extract_list_of_recommendation(rating_time_sim, similarity_sum)

def user_based(person_to_recommend, preference_space, number_of_items_to_recommend=10, similarity_measure='euclidean_distance'):

	""" return list of recommended items using user_based approach
	
	Args
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

	totals = {}
	similarity_sum = {}

	for other_person in preference_space:
		if other_person == person_to_recommend:
			continue
		from importlib import import_module
		sim_mod = import_module("recommender_engine.similarity_measure."  + similarity_measure)
		sim_func = getattr(sim_mod, similarity_measure)
		sim = sim_func(preference_space, person_to_recommend, other_person)

		if sim <= 0: 
			continue

		for item in preference_space[other_person]:
			if item not in preference_space[person_to_recommend] or preference_space[person_to_recommend][item]==0:
				totals.setdefault(item,0) #if item not in dict, will set default to 0
				totals[item] += sim * preference_space[other_person][item]
				similarity_sum.setdefault(item,0)
				similarity_sum[item] += sim

	return extract_list_of_recommendation(totals, similarity_sum, number_of_items_to_recommend)
	
def extract_list_of_recommendation(score, similarity_sum, number_of_items_to_recommend):
	results = []
	for item in score:
		try:
			rating = score[item] / similarity_sum[item]
		except ZeroDivisionError:
			results.append((0, item))
		else:
			results.append((rating, item))

	results.sort(key = lambda x: x[0], reverse=True)

	return [x[1] for x in results[0:number_of_items_to_recommend]]
	