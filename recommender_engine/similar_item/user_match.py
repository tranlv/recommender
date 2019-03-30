#!/usr/bin/env python
# -*- coding: utf-8 -*-

from importlib import import_module

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"

def user_match(preference_space, person_to_recommend, number_of_items_to_recommend=10, similarity_measure="euclidean_distance"):
	
	""" Return list of user that match given person 
			
		Args
		--------------
			preference_space (dict) keys are users while values are dictionary of items and ratings
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
	sim_mod = import_module("recommender.similarity_measure."  + similarity_measure)
	sim_func = getattr(sim_mod, similarity_measure)

	result = [(sim_func(preference_space, person_to_recommend, other), other) for other in preference_space if other != person_to_recommend]
	return result

		