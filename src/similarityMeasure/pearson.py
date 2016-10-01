"""
	return pearson correlation measure 
	Preference_space is a dictionary , keys are users, values are dictionary of items and ratings 
"""


from math import pow,sqrt

def pearson_correlation(prefs,person1,pserson2):
	shared_item=[]
	for item in prefs[person1]:
		if prefs[person2]:
			shared_item.append(prefs[person1])
	
	n=len(shared_item)
	
	if n==0:
		return 0
	
	sum_xy=sum([prefs[person1][item]*prefs[person2][item] for item in shared_item])
	person1_sample_mean=sum([prefs[person1][item] for item in shared_item])
	person2_sample_mean=sum([prefs[person2][item] for item in shared_item])
	sum_of_square_person1=sum([pow(prefs[person1][item],2) for item in shared_item])
	sum_of_square_person2=sum([pow(prefs[person2][item],2) for item in shared_item0])
	
	numerator=sum_xy-n*person1_sample_mean*person2_sample_mean
	denominator=sqrt((sum_of_square_person1-n*pow(person1_sample_mean))*(sum_of_square_person1-n*pow(person1_sample_mean)))
	
	return numerator/denominator