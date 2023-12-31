import pytest
from recommender.similar_item import find_similar_item


def test_find_similar_item_empty_preference_space():
    preference_space = {}
    results = find_similar_item(preference_space)
    assert results == {}


def test_find_similar_item_single_user_single_item():
    preference_space = {'user1': {'item1': 'rating1'}}
    results = find_similar_item(preference_space)
    assert results == {'item1': []}


def test_find_similar_item_multiple_users_multiple_items_euclidean_distance():
    preference_space = {
        'user1': {'item1': 0.1, 'item2': 0.2, 'item3': 0.3},
        'user2': {'item1': 0.2, 'item2': 0.3, 'item3': 0.4},
        'user3': {'item1': 0.3, 'item2': 0.4, 'item3': 0.5},
    }
    results = find_similar_item(
        preference_space, number_of_items_to_recommend=1, similarity_measure="euclidean_distance")
    assert results == {
        'item1': [(0.970873786407767, 'item2'), (0.8928571428571428, 'item3')],
        'item2': [(0.970873786407767, 'item1'), (0.970873786407767, 'item3')],
        'item3': [(0.8928571428571428, 'item1'), (0.970873786407767, 'item2')]
    }


def test_find_similar_item_multiple_users_multiple_items_cosine():
    preference_space = {
        'user1': {'item1': 1, 'item2': 2, 'item3': 3},
        'user2': {'item1': 2, 'item2': 3, 'item3': 4},
        'user3': {'item1': 3, 'item2': 4, 'item3': 5},
    }
    results = find_similar_item(
        preference_space, number_of_items_to_recommend=1, similarity_measure="cosine")
    assert results == {
        'item1': [(1.0, 'item2'), (1.0, 'item3')],
        'item2': [(1.0, 'item1'), (1.0, 'item3')],
        'item3': [(1.0, 'item1'), (1.0, 'item2')]
    }


def test_find_similar_item_multiple_users_multiple_items_pearson_correlation():
    preference_space = {
        'user1': {'item1': 1, 'item2': 2, 'item3': 3},
        'user2': {'item1': 2, 'item2': 3, 'item3': 4},
        'user3': {'item1': 3, 'item2': 4, 'item3': 5},
    }
    results = find_similar_item(
        preference_space, number_of_items_to_recommend=1, similarity_measure="pearson_correlation")
    assert results == {
        'item1': [(-1.5106382978723405, 'item2'), (-2.021276595744681, 'item3')],
        'item2': [(-0.6635514018691588, 'item1'), (-1.3364485981308412, 'item3')],
        'item3': [(-0.4973821989528796, 'item1'), (-0.7486910994764397, 'item2')]
    }
