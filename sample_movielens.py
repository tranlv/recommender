from recommender.recommender import recommender

"""
	This sample used movielens datasets @ https://grouplens.org/datasets/movielens/
"""

def make_preference_space_MovieLens(path):
	"""
		The function processes Movielens data set
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



def sample_movielens():
	"""
		Running the application using Movielens dataset:
	"""

	#Creating preference_space from Movieslen dataset
	preference_space = make_preference_space_MovieLens('../Movielens')
	model = recommender(preference_space = preference_space, recommender = 'user_based', 
						number_of_items_to_recommend = 10, similarity = 'euclidean_distance')
	print(model.make_recomendation('1'))


if __name__=="__main__":
	sample_movielens()