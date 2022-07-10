# **Recommender**

<p align="center">
	<a href="https://pypi.org/project/recommender-engine/"><img src="https://img.shields.io/pypi/v/recommender-engine.svg"></a>
	<a href="https://pepy.tech/project/recommender-engine"><img src="https://pepy.tech/badge/recommender-engine"></a>
	<a href="https://saythanks.io/to/vutransingapore"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"></a>
</p>

---

Recommender is a recommendation application using either item-based or user-based approaches.

Recommender is at version [v0.3.0](https://github.com/tranlyvu/recommender/releases), also see [change log](https://github.com/tranlyvu/recommender/blob/dev/CHANGELOG.md) for more details on release history.

If you like this project, feel fee to leave a few words of appreciation here [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/vutransingapore%40gmail.com)

| Build | [![Build Status][3]][4] | [![Coverage Status][5]][6] |
| :--- | :--- | :---  |
| **Quality** | [![Maintainability][13]][14] | |
| **Platform** | [![pyversion][25]][26] | [![implementation][27]][28] |

[3]: https://travis-ci.org/tranlyvu/recommender.svg?branch=dev
[4]: https://travis-ci.org/tranlyvu/recommender
[5]: https://coveralls.io/repos/github/tranlyvu/recommender/badge.svg?branch=dev
[6]: https://coveralls.io/github/tranlyvu/recommender?branch=dev
[13]: https://api.codeclimate.com/v1/badges/de05d6acb8cd3b11aa0c/maintainability
[14]: https://codeclimate.com/github/tranlyvu/recommender/maintainability
[25]: https://img.shields.io/pypi/pyversions/recommender-engine.svg
[26]: https://pypi.org/project/recommender-engine/
[27]: https://img.shields.io/pypi/implementation/recommender-engine.svg
[28]: https://pypi.org/project/recommender-engine/

---
Table of contents
---

1. [Usage](#Usage)
2. [Contribution](#Contribution) 
4. [License](#License)

---
Usage
---

Install with pip

```
$ pip install recommender-engine
```

### API

make_recommendation(person_to_recommend, preference_space, recommender_approach='user_based', number_of_items_to_recommend=10, similarity_measure='euclidean_distance')

```	
	Return list of recommendation items based on the chosen approach and similarity emasure

	Parameters
	--------------
	person_to_recommend (str): user id/name to recommend to

	preference_space (dict):  keys are user id/name and values are dictionary of items and ratings

	recommender_approach (str): support 'user_based' (default) or 'item_based'

	number_of_items_to_recommend (int): number of items to recommend (default=10)

	similarity_measure (str): similarity measurement method , support 'euclidean_distance' (default), 'cosine' or 'pearson_correlation'
```

### Example

```
>>> from recommender_engine import make_recommendation
>>>	result = make_recommendation(person_to_recommend = "userA",
                                 preference_space = preference_space,
                                 recommender_approach = 'user_based',
                                 number_of_items_to_recommend = 10,
                                 similarity_measure = 'euclidean_distance')
```

The preference space is dictionary data structure where keys are users and values are dictionary of items and ratings

```
preference_space = { 'userA : { 'item1' : 'ratingA1, 
                                 'item2' : 'ratingA2',
                                 ...}, 
                     ... 
                     'userZ: { 'item1' : 'ratingZ1,
                              'item2' : 'ratingZ2',
							  ...}
                    }
```

### Tested Datasets

The project has been tested on these Datasets

1. [Jester](http://goldberg.berkeley.edu/jester-data)
2. [MovieLens](http://files.grouplens.org/datasets/movielens/)

---
Contribution 
---

Please follow our contribution convention at [contribution instruction](https://github.com/tranlyvu/recommender/blob/dev/CONTRIBUTING.md) and [code of conduct](https://github.com/tranlyvu/recommender/blob/dev/CODE-OF-CONDUCT.md)

Please check out the [issue file](https://github.com/tranlyvu/recommender/blob/dev/ISSUES.md) for list of issues that required helps.

### Appreciation

Feel free to add your name into the [list of contributors](https://github.com/tranlyvu/recommender/blob/dev/CONTRIBUTORS.md).

If you like this project, you can buy buy me a [pizza](https://www.buymeacoffee.com/tranlv) to motivate me improve on the project.

---
License
---

See the [LICENSE](https://github.com/tranlyvu/recommender/blob/master/LICENSE) file for license rights and limitations (Apache License 2.0).


