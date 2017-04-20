========
recommender-engine
========
A simple recommender application using either item-based or user-based approaches

Using recommender-engine
===============
- Downloading a release_.

.. _release: https://github.com/tranlyvu/recommender-engine

- Quickstart

1. Create preference_space: dictionary type, keys are users while values are dictionary of items and ratings
    ie. preference_space={'userA:{'item1':'ratingA1,'item2':'ratingA2'....'itemn':'ratingAn},
							'userB:{'item1':'ratingB1,'item2':'ratingB2'....'itemn':'ratingBn},								 'userZ:{'item1':'ratingZ1,'item2':'ratingZ2'....'itemn':'ratingZn},
										}
2.	Initializing class 'recommender'
3.	Calling 'make_recommender' method to make recommendation 
	
- Sample

.. _sample: https://github.com/tranlyvu/recommender/blob/master/sample_jester.py

Contribution
============
- Join our gitter_ .

.. _gitter: https://gitter.im/recommender-enginer
- For any feature recommendation please register a blueprint_.

.. _blueprint: https://blueprints.launchpad.net/recommender-engine
- For bug reports or requests please submit an issue_.

.. _issue: https://github.com/tranlyvu/recommender-engine/issues

Frequently Asked Questions
==========================
- The FAQs can be found on the project's Wiki_ page. Feel free to submit more questions to be answered and added to the page.

.. _Wiki: https://github.com/tranlyvu/recommender-engine/wiki

License
=======
See the LICENSE_ file for license rights and limitations (Apache License 2.0).

.. _LICENSE: https://github.com/tranlyvu/recommender-engine/blob/master/LICENSE

