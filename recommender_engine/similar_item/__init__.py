"""
	recommender_engine
	-----
	recommender_engine is a recommendation application using either item-based or user-based approaches

	:copyright: (c) 2016 - 2019 by Tran Ly Vu. All Rights Reserved.
    :license: Apache License 2.0
"""

from .find_similar_item import find_similar_item
from .preference_space_transform import preference_space_transform
from .user_match import user_match

name="similar_item"
__all__ = ["find_similar_item", "preference_space_transform", "user_match"]
__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
__credits__ = ["Tran Ly Vu"]
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"