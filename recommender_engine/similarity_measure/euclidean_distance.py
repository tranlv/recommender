#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide euclidean_distance function to calculate euclidean distance"""

from __future__ import division			
from math import pow	

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"
		
def euclidean_distance(preference_space, person1, person2):
	
	""" Return euclidean distance measure @ https://en.wikipedia.org/wiki/Euclidean_distance
		
		Args
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
	

	number = 0
	for item in preference_space[person1]:
		if item in preference_space[person2]:
			number = number+ 1
		else:
			continue
			
	if number == 0:
		return 0 
		
	sum_of_square = sum([pow(preference_space[person1][item]-preference_space[person2][item],2) 
					for item in preference_space[person1] if item in preference_space[person2]])
	
	return 1/(1+sum_of_square)	
