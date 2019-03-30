"""
	recommender_engine
	-----
	recommender_engine is a recommendation application using either item-based or user-based approaches

	:copyright: (c) 2016 - 2019 by Tran Ly Vu. All Rights Reserved.
    :license: Apache License 2.0
"""
from .cosine import cosine
from .euclidean_distance import euclidean_distance
from .pearson_correlation import pearson_correlation

name="similarity_measure"
__all__ = ["cosine", "euclidean_distance", "pearson_correlation"]
__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"
