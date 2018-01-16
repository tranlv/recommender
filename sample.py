from recommender.recommender import recommender
from xlrd import open_workbook

"""
	This sample used jester and movielens as sample datasets, you can download dataset as
	
	https://grouplens.org/datasets/movielens/
	http://goldberg.berkeley.edu/jester-data/

"""

def merge_preference_space(*prefs_space):
	"""
		The function merge all the preference spaces into one
	"""
	result = {}
	for space in prefs_space:
		result.update(space)
	
	return result

def make_preference_space(raw_data, start):
	"""
		create preference_space from raw data
		the data structure is dictionary with keys are users and values are dictionaries of items and ratings
	"""
	preference_space = {}
	for row in range(0,raw_data.nrows):	
		preference_space[str('user ' + str(start + row))] = {}	
		for col in range(1,raw_data.ncols):
			if raw_data.cell_value(row,col) == 99: continue
			preference_space[str('user ' + str(start + row))]['joke ' + str(col)] = float(raw_data.cell_value(row, col))		
	
	return preference_space


def make_preference_space_Jester(file_path):
	"""
		The function takes in 3 jester dataset files and then merge the file
	"""
	
	raw_data_1 = open_workbook(file_path + '/jester-data-1.xls').sheets()[0]
	prefs_space_1 = make_preference_space(raw_data_1, 0)
	raw_data_2 = open_workbook(file_path + '/jester-data-2.xls').sheets()[0]
	prefs_space_2 = make_preference_space(raw_data_2, raw_data_1.nrows)
	raw_data_3 = open_workbook(file_path + '/jester-data-3.xls').sheets()[0]
	prefs_space_3 = make_preference_space(raw_data_3,raw_data_1.nrows + raw_data_2.nrows)
	
	return merge_preference_space(prefs_space_1, prefs_space_2, prefs_space_3)
	

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


def sample_jester():
	"""
		Running the application using Jester dataset:
	"""

	#Creating preference_space from Jester dataset
	preference_space = make_preference_space_Jester('../data/Jester')
	model = recommender(preference_space, recommender = 'user_based', 
					number_of_items_to_recommend = 5, similarity = 'euclidean_distance')
	print(model.make_recomendation('user 36681'))

def sample_movielens():
	"""
		Running the application using Movielens dataset:
	"""

	#Creating preference_space from Movieslen dataset
	preference_space = make_preference_space_MovieLens('../data/Movielens')
	model = recommender(preference_space = preference_space, recommender = 'user_based', 
						number_of_items_to_recommend = 10, similarity = 'euclidean_distance')
	print(model.make_recomendation('1'))

def main():
	sample_jester()
	sample_movielens()


if __name__=="__main__":
	main()