#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Prove cosine function to calculate cosine"""

from __future__ import division
from math import sqrt

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"

def cosine(preference_space, person1, person2):
	
	""" return cosine similarity measure @ https://en.wikipedia.org/wiki/Cosine_similarity
	
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
	
	Raises
	--------------
		ZeroDivisionError

	"""

	common_interest = [x for x in preference_space[person1] if x in preference_space[person2]]
	vector1 = list(map(lambda x: 1 if x in common_interest else 0, preference_space[person1]))
	vector2 = list(map(lambda x: 1 if x in common_interest else 0, preference_space[person2]))
	
	sumxx = 0
	for i in range(len(vector1)):
		x = vector1[i]
		sumxx += x*x
	
	sumyy = 0
	for i in range(len(vector2)):
		y = vector2[i]
		sumyy += y*y

	denominator = sqrt(sumxx * sumyy)

	numerator = 0
	for i in range(min(len(vector1), len(vector2))):
		x,y = vector1[i], vector2[i]
		numerator += x*y

	if denominator == 0:
		return 0
	else:
		return numerator/denominator
