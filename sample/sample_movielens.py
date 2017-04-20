"""
	Running the application using Movielens dataset
"""

from recommender import *

def main():
	#Creating preference_space from Movielen dataset:
	preference_space=make_preference_space_MovieLens('/recommender/data/Movielens')
	model=recommender(preference_space=preference_space,recommender='user_based',number_of_items_to_recommend=10,similarity='euclidean_distance')
	print(model.make_recomendation('1'))
	
if __name__=="__main__":
	main()