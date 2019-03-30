#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .user_match import user_match
from .preference_space_transform import preference_space_transform

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"

def find_similar_item(preference_space, number_of_items_to_recommend=10, similarity_measure="euclidean_distance"):
	
	""" Return list of similar item for each item in preference space
		The function transform the preference space before checking each item
	
	Args
	--------------
		preference_space (dict) keys are users while values are dictionary of items and ratings
						ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
											  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
											   .....
											  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
												}

		number_of_items_to_recommend (int): number of items to recommend (default=10)
		
		similarity_measure (str): similarity measurement method, support 'euclidean_distance' (default), 'cosine' or 'pearson_correlation'
	
	Returns
	--------------	
    	dict

	"""

	results = {}
	transformed_preference_space = preference_space_transform(preference_space)
	
	for item in transformed_preference_space:
		results[item] = user_match(transformed_preference_space, item, number_of_items_to_recommend, similarity_measure)			
	
	return results
