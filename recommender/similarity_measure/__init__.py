"""
	The module recommender.similarityMeasure includes different similarity measure
"""

from .cosine import cosine
from .euclidean import euclidean_distance
from .pearson import pearson_correlation

__all__=['cosine',
		 'euclidean_distance',
		 'pearson_correlation'
		]

__version__ = '1.0.0'
