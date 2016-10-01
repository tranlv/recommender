#Overview:
A simple recommender application using either item-based or user-based approaches

#Usage:
*	Samples
	1.	[Jester](https://github.com/tranlyvu/recommender/blob/master/sample_jester.py)
	2.	[Movielens](https://github.com/tranlyvu/recommender/blob/master/sample_movielens.py)

* 	Quickstart
	1. Create preference_space: dictionary type, keys are users while values are dictionary of items and ratings
				   ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2'....'itemn':'ratingAn},
							'userB:{'item1':'ratingB1,'item2':'ratingB2'....'itemn':'ratingBn},								 'userZ:{'item1':'ratingZ1,'item2':'ratingZ2'....'itemn':'ratingZn},
										}
	2.	Initializing class 'recommender'
	3.	Calling 'make_recommender' method to make recommendation 
	
#Datasets for samples:
*	[Movielens](http://grouplens.org/datasets/movielens/) : 1,000,000 integer ratings (from 1-5) of 3500 films from 6,040 users. 
*	[Jester](http://goldberg.berkeley.edu/jester-data/) : 1 Million continuous ratings (-10.00 to +10.00) of 100 jokes from 73,421 users collected between April 1999 - May 2003

#Reference:
*  [Programming Collective Intelligence](http://shop.oreilly.com/product/9780596529321.do)
*  [Recommender Systems Handbook](http://www.springer.com/gp/book/9780387858203)

#Contribution
Contributions are welcome! For bug reports or requests please submit an [issue](https://github.com/tranlyvu/recommender/issues).

#Contact-info
Feel free to contact me to discuss any issues, questions, or comments.
*  Email: vutransingapore@gmail.com
*  Twitter: [@vutransingapore](https://twitter.com/vutransingapore)
*  GitHub: [vutransingapore](https://github.com/tranlyvu)

#License
See the LICENSE file for license rights and limitations (MIT).
