"""
	Recommender
	-----
	recommender is a recommendation application using either item-based or user-based approaches

	:copyright: (c) 2016 - 2019 by Tran Ly Vu. All Rights Reserved.
    :license: Apache License 2.0
"""

from .similarity_measure import (
	cosine,
	euclidean_distance,
	pearson_correlation	
)

from .similar_item import (
	find_similar_item,
	preference_space_transform,
	user_match
)

__all__=[
		'dataHandle',
		'recommenderEngine',
		'similarItem',
		'similarityMeasure'
		]	

__version__ = '1.1.0'
__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
