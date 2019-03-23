#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide pearson_correlation function to calculate pearson correlation"""

from __future__ import division
from math import pow,sqrt

__version__ = '1.1.1'
__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Production"

def pearson_correlation(prefs, person1, person2):
	""" return pearson correlation measure 
		
	Parameters
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
	
	shared_item=[]
	for item in prefs[person1]:
		if prefs[person2]:
			shared_item.append(prefs[person1])
	
	n=len(shared_item)
	
	if n==0:
		return 0
	
	sum_xy=sum([prefs[person1][item]*prefs[person2][item] for item in shared_item])
	person1_sample_mean=sum([prefs[person1][item] for item in shared_item])
	person2_sample_mean=sum([prefs[person2][item] for item in shared_item])
	sum_of_square_person1=sum([pow(prefs[person1][item],2) for item in shared_item])
	sum_of_square_person2=sum([pow(prefs[person2][item],2) for item in shared_item0])
	
	numerator=sum_xy-n*person1_sample_mean*person2_sample_mean
	denominator=sqrt((sum_of_square_person1-n*pow(person1_sample_mean))*(sum_of_square_person1-n*pow(person1_sample_mean)))
	
	return numerator/denominator