"""
	recommender_engine
	-----
	recommender_engine is a recommendation application using either item-based or user-based approaches

	:copyright: (c) 2016 - 2019 by Tran Ly Vu. All Rights Reserved.
    :license: Apache License 2.0
"""


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='recommender-engine',
    version="0.3.0",
    author='Tran Ly Vu',
	author_email='vutransingapore@gmail.com',
	maintainer='Tran Ly Vu <vutransingapore@gmail.com>',
	maintainer_email='vutransingapore@gmail.com',
	description='A recommendation application using either item-based or user-based approaches',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/tranlyvu/recommender',
	packages=find_packages(exclude=("*.tests", "*.tests.*", "tests.*", "tests", "docs")),
	license='Apache License 2.0',
  	download_url='https://github.com/tranlyvu/recommender/releases', 
  	zip_safe=False,
	include_package_data=True,
	platforms="any",
    classifiers=[
    	'Programming Language :: Python :: 2',
    	'Programming Language :: Python :: 2.7',
    	'Programming Language :: Python :: 3',
    	'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		"License :: OSI Approved :: Apache Software License ",
		"Operating System :: POSIX",
		"Operating System :: POSIX :: Linux",
		"Operating System :: Unix",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Science/Research",
		"Intended Audience :: End Users/Desktop",
		"Intended Audience :: Developers",
		"Natural Language :: English",
		"Environment :: Console",
		"Topic :: Scientific/Engineering",
		"Topic :: Scientific/Engineering :: Artificial Intelligence",
		"Topic :: Scientific/Engineering :: Information Analysis",
		"Topic :: Education",
		"Programming Language :: Python :: Implementation :: CPython",
		"Programming Language :: Python :: Implementation :: PyPy",
		"Framework :: Pytest"
	],
	keywords=['Recommender', "Artificial Intelligence", "Data Science"],
	project_urls={
	    'Source': 'https://github.com/tranlyvu/recommender',
	    'Tracker': 'https://github.com/tranlyvu/recommender/issues',
	    'Chat: Gitter': 'https://gitter.im/recommender/Lobby',
	    'CI: Travis': 'https://travis-ci.org/tranlyvu/recommender',
	    'Coverage: coveralls': 'https://coveralls.io/github/tranlyvu/recommender',
	},
	py_modules=["six"],
	python_requires='>=2.7, <4',
	tests_require = [
    	'pytest',
    	'python-coveralls'
    ]
)
