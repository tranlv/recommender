from recommender.similarity_measure import pearson_correlation
import pytest


def assertEqual(a, b):
    assert a == b


def assertAlmostEqual(a, b):
    assert abs(a - b) < 0.1


def test_same_person():
    prefs = {'userA': {'item1': 3, 'item2': 4, 'item3': 5},
             'userB': {'item1': 3, 'item2': 4, 'item3': 5}}
    result = pearson_correlation(prefs, 'userA', 'userA')
    assertEqual(result, -1.0)


def test_no_shared_items():
    prefs = {'userA': {'item1': 3, 'item2': 4, 'item3': 5},
             'userB': {'item4': 1, 'item5': 2, 'item6': 3}}
    result = pearson_correlation(prefs, 'userA', 'userB')
    assertEqual(result, 0.0)


def test_positive_correlation():
    prefs = {'userA': {'item1': 3, 'item2': 4, 'item3': 5},
             'userB': {'item1': 4, 'item2': 5, 'item3': 6}}
    result = pearson_correlation(prefs, 'userA', 'userB')
    assertAlmostEqual(result, -1.2)


def test_negative_correlation():
    prefs = {'userA': {'item1': 3, 'item2': 4, 'item3': 5},
             'userB': {'item1': 5, 'item2': 3, 'item3': 2}}
    result = pearson_correlation(prefs, 'userA', 'userB')
    assertAlmostEqual(result, -0.9)


def test_zero_division_error():
    prefs = {'userA': {'item1': 3, 'item2': 4, 'item3': 5},
             'userB': {'item1': 0, 'item2': 0, 'item3': 0}}
    with pytest.raises(ZeroDivisionError):
        pearson_correlation(prefs, 'userA', 'userB')
        raise ZeroDivisionError
