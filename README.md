# **recommender** [![HitCount][1]][2] 

[1]: http://hits.dwyl.io/tranlyvu/recommender.svg
[2]: http://hits.dwyl.io/tranlyvu/recommender

| Build | [![Build Status][3]][4] | [![Coverage Status][5]][6] | | 
| :--- | :--- | :---  | :--- |
| **Quality** | [![Maintainability][13]][14] | [![Requirements Status][19]][20] | |
| **Support** | [![Join the chat at https://gitter.im/find-link/Lobby][17]][18] | [![Open Source Helpers][7]][8] |  |

[3]: https://travis-ci.org/tranlyvu/recommender.svg?branch=dev
[4]: https://travis-ci.org/tranlyvu/recommender
[5]:https://coveralls.io/repos/github/tranlyvu/recommender/badge.svg?branch=dev
[6]: https://coveralls.io/github/tranlyvu/recommender?branch=dev

[13]: https://api.codeclimate.com/v1/badges/de05d6acb8cd3b11aa0c/maintainability
[14]: https://codeclimate.com/github/tranlyvu/recommender/maintainability


[19]: https://requires.io/github/tranlyvu/recommender/requirements.svg?branch=dev
[20]: https://requires.io/github/tranlyvu/recommender/requirements/?branch=dev

[17]: https://badges.gitter.im/gitterHQ/gitter.png
[18]: https://gitter.im/recommender-engine
[7]: https://www.codetriage.com/tranlyvu/recommender/badges/users.svg
[8]: https://www.codetriage.com/tranlyvu/recommender

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
Contribution
---

Please follow [contribution instruction](https://github.com/tranlyvu/recommender/blob/dev/CONTRIBUTING.md) and [code of conduct](https://github.com/tranlyvu/recommender/blob/dev/CODE-OF-CONDUCT.md)

### Development setup

recommender was developed with Python 3.6. Simply run the following on your development environment:

```
$pip install -r requirement.txt
```
Or to set up environment with virtualenv

```
$ cd <path to recommender project>
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

If you are done working in the virtual environment for the moment, you can deactivate it:

```
$ deactivate
```
### [List of contributors](https://github.com/tranlyvu/recommender/blob/dev/CONTRIBUTORS.md)

### Hall of Fame

[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/images/0)](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/links/0)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/images/1)](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/links/1)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/images/2)](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/links/2)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/images/3)](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/links/3)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/images/4)](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/links/4)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/images/5)](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/links/5)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/images/6)](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/links/6)[![](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/images/7)](https://sourcerer.io/fame/tranlyvu/tranlyvu/recommender/links/7)


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
Contact
---

Feel free to contact me to discuss any issues, questions, or comments.
*  Email: vutransingapore@gmail.com
*  Linkedln: [@vutransingapore](https://www.linkedin.com/in/tranlyvu/)
*  GitHub: [Tran Ly Vu](https://github.com/tranlyvu)
*  Blog: [tranlyvu.github.io](https://tranlyvu.github.io/)

---
License
---

See the [LICENSE](https://github.com/tranlyvu/recommender/blob/master/LICENSE) file for license rights and limitations (Apache License 2.0).


