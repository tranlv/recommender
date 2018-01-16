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

__version__ = '1.0.0'
