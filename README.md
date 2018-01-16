# **recommender**

[![Build Status](https://travis-ci.org/tranlyvu/recommender.svg?branch=master)](https://travis-ci.org/tranlyvu/recommender) [![Code Health](https://landscape.io/github/tranlyvu/recommender/master/landscape.svg?style=flat)](https://landscape.io/github/tranlyvu/recommender/master) [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/recommender-engine)

A recommendation application using either item-based or user-based approaches.

<img src="img/recommender.png" width="480" alt="Combined Image" />

---
Usage
---

- Downloading a [release](https://github.com/tranlyvu/recommender/releases) or fork the source code: 

```
$git clone https://github.com/tranlyvu/recommender.git
```

- The simplest way is to look at the [sample file](https://github.com/tranlyvu/recommender/tree/master/sample) for usage and run it. Plese download the 2 datasets, Jester ([here](http://goldberg.berkeley.edu/jester-data/jester-data-1.zip), [here](http://goldberg.berkeley.edu/jester-data/jester-data-2.zip) and [here](http://goldberg.berkeley.edu/jester-data/jester-data-3.zip)) and [MovieLens](http://files.grouplens.org/datasets/movielens/ml-10m.zip) to use as sample datasets before running it.

- Note that the preference space is dictionary data structure where keys are users and values are dictionary of items and ratings; i.e. preference_space = {'userA : {'item1' : 'ratingA1, 'item2' : 'ratingA2'..., 'itemn' : 'ratingAn}, ..., 'userZ:{'item1' : 'ratingZ1, 'item2' : 'ratingZ2'..., 'itemn' : 'ratingZn}}

---
Development Setup
---

recommender was developed with Python 3.6. Simply run the following on your development environment:

```
$pip install -r requirement.txt
```

---
Project Architecture
---

To do

---
Release History
---

* v1.0.0 - Jan 16, 2018
	* First official release

---
Contribution
---

For bug reports or requests please submit an [issue](https://github.com/tranlyvu/recommender/issues).

For new features contribution, please follow the following instruction:

```
1. Fork the source code (`$git clone https://github.com/tranlyvu/recommender.git`)
2. Create your feature branch (`$git checkout -b new/your-feature`)
3. Commit your changes (`$git commit -am 'Add some new feature'`)
4. Push to the branch (`$git push origin new/your-feature`)
5. Create a new Pull Request at https://github.com/tranlyvu/recommender/pulls
```

---
Contact
---

Feel free to contact me to discuss any issues, questions, or comments.
*  Email: vutransingapore@gmail.com
*  Twitter: [@vutransingapore](https://twitter.com/vutransingapore)
*  GitHub: [Tran Ly Vu](https://github.com/tranlyvu)

---
License
---

See the [LICENSE](https://github.com/tranlyvu/recommender/blob/master/LICENSE) file for license rights and limitations (Apache License 2.0).


