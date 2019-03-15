# **recommender** [![HitCount][1]][2] [![star this repo][21]][22] [![fork this repo][23]][24] 

[1]: http://hits.dwyl.io/tranlyvu/recommender.svg
[2]: http://hits.dwyl.io/tranlyvu/recommender
[21]: http://githubbadges.com/star.svg?user=tranlyvu&repo=recommender&style=default
[22]: https://github.com/tranlyvu/recommender
[23]: http://githubbadges.com/fork.svg?user=tranlyvu&repo=recommender&style=default
[24]: https://github.com/tranlyvu/recommender/fork

| Build | [![Build Status][3]][4] | [![Coverage Status][5]][6] |
| :--- | :--- | :---  |
| **Quality** | [![Maintainability][13]][14] | [![Requirements Status][19]][20] |
| **Support** | [![Join the chat at https://gitter.im/find-link/Lobby][17]][18] |  |

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


A recommendation application using either item-based or user-based approaches.

<img src="img/recommender.png" width="480" alt="Combined Image" />

---
Table of contents
---

1. [Usage](#Usage)
2. [Contribution](#Contribution) 
3. [Project Architecture](#Project-Architecture)
4. [Release History](#Release-History)
5. [Contact](#Contact)
6. [License](#License)

---
Usage
---

- Downloading a [release](https://github.com/tranlyvu/recommender/releases)

### API

### Example

- The preference space is dictionary data structure where keys are users and values are dictionary of items and ratings; i.e. 

```
preference_space = {
					'userA : {
							 'item1' : 'ratingA1, 
							 'item2' : 'ratingA2',
							  ..., 
							  'itemn' : 'ratingAn
							  }, 
					..., 
					'userZ:{
							'item1' : 'ratingZ1,
							 'item2' : 'ratingZ2',
							  ...,
							 'itemn' : 'ratingZn
							}
				    }
```

### Tested Datasets

The project has been tested on these Datasets

1. [Jester](http://goldberg.berkeley.edu/jester-data)
2. [MovieLens](http://files.grouplens.org/datasets/movielens/)

---
Contribution[![Open Source Helpers][7]][8] 
---
[7]: https://www.codetriage.com/tranlyvu/recommender/badges/users.svg
[8]: https://www.codetriage.com/tranlyvu/recommender

Please follow our contribution convention at [contribution instruction](https://github.com/tranlyvu/recommender/blob/dev/CONTRIBUTING.md) and [code of conduct](https://github.com/tranlyvu/recommender/blob/dev/CODE-OF-CONDUCT.md)

### List of issues

1. Update unit test ([#2](https://github.com/tranlyvu/recommender/issues/2))

### Appreciation

Feel free to add your name into the [list of contributors](https://github.com/tranlyvu/recommender/blob/dev/CONTRIBUTORS.md). You will automatically be inducted into Hall of Fame as a way to show my appreciation for your contributions

#### Hall of Fame

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

If you like my project, feel fee to leave a few words of appreciation here [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/tranlyvu)

---
License
---

See the [LICENSE](https://github.com/tranlyvu/recommender/blob/master/LICENSE) file for license rights and limitations (Apache License 2.0).


