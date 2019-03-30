#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"

def preference_space_transform(preference_space):
	
	""" The function takes in preference space with keys are users and transform it 

	Args
	--------------

		preference_space (dict):  keys are user Id's and values are dictionary of items and ratings
						ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
											  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
											   .....
											  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
												}

	Returns
	--------------	

		dict
	"""


	transform = {}
	for person in preference_space:
		for item in preference_space[person]:
			transform[item] = {}
			transform[item][person] = preference_space[person][item]

	return transform
	