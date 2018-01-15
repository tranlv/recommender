from .similarity_measure import *


class recommender:
	def __init__(self,preference_space,recommender='user_based',
				number_of_items_to_recommend=10,similarity='euclidean_distance'):
		"""Generate recommender	algorithms	
		Parameters
		--------------
		preference_space: dictionary type, keys are users while values are dictionary of items and ratings
						ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2....'itemn':'ratingAn},
											  'userB:{'item1':'ratingB1,'item2':'ratingB2....'itemn':'ratingBn},
											   .....
											  'userZ:{'item1':'ratingZ1,'item2':'ratingZ2....'itemn':'ratingZn},
													}
		recommender : string, 'user_based' (default) or 'item_based'

		number_of_items_to_recommend: integer(default=10)

		similarity : string, 'euclidean_distance' (default), 'cosine' or 'pearson_correlation'

		Returns
		--------------	
		self : object
		   Returns self.
		"""
		algorithms_string=['user_based','item_based']
		algorithms_list=[user_based,item_based]	
		similarity_string=['euclidean_distance','cosine','pearson_correlation']
		similarity_list=[euclidean_distance,cosine,pearson_correlation]
		
		if not isinstance(preference_space,dict) :
			raise TypeError("preference space is not dictionary type!")	
		self.my_preference_space=preference_space
		
		
		try: 
			algorithms_string.index(recommender)
		except ValueError:
			print(recommender+" is not one of accepted recommender engine, using user-based by default!")
			recommender='user_based'
		finally:	
			self.recommender=algorithms_list[algorithms_string.index(recommender)]
		
		try: 
			similarity_string.index(similarity)
		except ValueError:
			print(similarity+" is not one of accepted similarity measure, using euclidean_distance by default!")
			similarity='euclidean_distance'
		finally:	
			self.similarity=similarity_list[similarity_string.index(similarity)]
		
		
		self.number_of_item=number_of_items_to_recommend

	
	def make_recomendation(self,user):
	
		""" return items recommended
		Parameters
		--------------
		user: string
	
		Returns
		--------------	
		List of recommended items
		"""
		
		if self.number_of_item==0:
			return 
			
		return self.recommender(preference_space=self.my_preference_space,person_to_recommend=user,
								number_of_items=self.number_of_item,similarity=self.similarity)
