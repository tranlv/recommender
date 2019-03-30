from recommender_engine import make_recommendation

"""
	This sample used movielens datasets @ http://files.grouplens.org/datasets/movielens/ml-10m.zip
"""

def make_preference_space_MovieLens(path):
	""" create preference space for Movielens data set
	"""
	
	movies = {}
	for line in open(path + '/movies.dat'):
		(movieid, title) = line.split('::')[0:2]
		movies[movieid] = title
	
	preference_space = {}
	for line in open(path + '/ratings.dat'):
		(user, movieid, rating, ts) = line.split('::')
		preference_space.setdefault(user, {})
		preference_space[user][movies[movieid]] = float(rating)
	
	return preference_space


def movielens():
	""" Running the application using Movielens dataset
	"""

	#Creating preference_space from Movieslen dataset
	preference_space = make_preference_space_MovieLens('../Movielens')

	result = make_recommendation(person_to_recommend='1', 
                                 preference_space = preference_space, 
							     recommender_approach = 'user_based', 
							     number_of_items_to_recommend = 10,
							     similarity_measure = 'cosine')
	print(result)	

if __name__=="__main__":
	movielens()