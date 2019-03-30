from recommender_engine import make_recommendation
from xlrd import open_workbook

"""
	This sample used jester dataset @ http://goldberg.berkeley.edu/jester-data/
"""

def make_preference_space(raw_data, start):
	
	""" create preference_space from raw data

		Args:
			raw_data
			start

		Returns:
			dict: keys are users and values are dictionaries of items and ratings
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

	result = {}
	for space in [prefs_space_1, prefs_space_2, prefs_space_3]:
		result.update(space)
	
	return result
	

def jester():
	"""
		Running the application using Jester dataset:
	"""

	#Creating preference_space from Jester dataset
	preference_space = make_preference_space_Jester('../Jester')
	result = make_recommendation('user 36681', preference_space, 
								recommender_approach = 'user_based', 
								number_of_items_to_recommend = 5, 
								similarity_measure = 'euclidean_distance')
	print(result)


if __name__=="__main__":
	jester()