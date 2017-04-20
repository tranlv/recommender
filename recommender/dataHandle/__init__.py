"""
  The module recommender.dataHandle includes data processing for sample tests
"""

from .jester import make_preference_space_Jester
from .movielens import make_preference_space_MovieLens

__all__=[
			'make_preference_space_Jester',
			'make_preference_space_MovieLens'
		]