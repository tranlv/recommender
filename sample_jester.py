"""
	Running the application using Jester dataset:
"""

from src.dataHandle import *
from src.recommender import recommender

def main():
	#Creating preference_space from fromJester dataset:
	preference_space=make_preference_space_Jester('/github/recommender/data/Jester')
	model=recommender(preference_space,recommender='user_based',number_of_items_to_recommend=5,similarity='euclidean_distance')
	print(model.make_recomendation('user 36681'))
	
if __name__=="__main__":
	main()