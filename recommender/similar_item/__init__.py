"""
	The module recommender.similarItem includes 
"""

from .find_similar_item import find_similar_item
from .preference_space_transform import preference_space_transform
from .user_match import user_match


__all__= ['find_similar_item',
		'preference_space_transform',
		 'user_match'
		]

__version__ = '1.0.0'
