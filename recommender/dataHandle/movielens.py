"""
	The function processes Movielens data set
"""

def make_preference_space_MovieLens(path):
	movies={}
	for line in open(path+'/movies.dat'):
		(movieid,title)=line.split('::')[0:2]
		movies[movieid]=title
	
	preference_space={}
	for line in open(path+'/ratings.dat'):
		(user,movieid,rating,ts)=line.split('::')
		preference_space.setdefault(user,{})
		preference_space[user][movies[movieid]]=float(rating)
	return preference_space

