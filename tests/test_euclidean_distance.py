import pytest
from recommender.similarity_measure import euclidean_distance


def test_euclidean_distance_empty_preference_space():
    preference_space = {'userA': {}, 'userB': {}}
    assert euclidean_distance(preference_space, 'userA', 'userB') == 0


def test_euclidean_distance_single_user():
    preference_space = {'userA': {'item1': 1}, 'userB': {}}
    assert euclidean_distance(preference_space, 'userA', 'userB') == 0


def test_euclidean_distance_different_length_ratings():
    preference_space = {
        'userA': {'item1': 1, 'item2': 2},
        'userB': {'item1': 1},
    }
    assert euclidean_distance(preference_space, 'userA', 'userB') == 1


def test_euclidean_distance_no_common_ratings():
    preference_space = {
        'userA': {'item1': 1, 'item2': 2},
        'userB': {'item3': 3, 'item4': 4},
    }
    assert euclidean_distance(preference_space, 'userA', 'userB') == 0


def test_euclidean_distance_positive_euclidean_distance():
    preference_space = {
        'userA': {'item1': 1, 'item2': 2, 'item3': 3},
        'userB': {'item1': 2, 'item2': 3, 'item3': 0},
    }
    assert euclidean_distance(preference_space, 'userA', 'userB') == 1 / 12
