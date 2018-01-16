"""
	The function takes in preference space with keys are users and transform it 
into another space where keys are items and values are users
"""

def preference_space_transform(preference_space):
	transform = {}
	for person in preference_space:
		for item in preference_space[person]:
			transform[item] = {}
			transform[item][person] = preference_space[person][item]
	return transform
	