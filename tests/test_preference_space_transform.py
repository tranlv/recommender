from recommender.similar_item import preference_space_transform
import pytest


def test_preference_space_transform_empty_input():
    """Test case 1: Empty preference_space."""
    preference_space = {}
    transformed_preference_space = preference_space_transform(preference_space)
    assert transformed_preference_space == {}


def test_preference_space_transform_single_user_single_item():
    """Test case 2: One user, one item."""
    preference_space = {'user1': {'item1': 'rating1'}}
    transformed_preference_space = preference_space_transform(preference_space)
    assert transformed_preference_space == {'item1': {'user1': 'rating1'}}


def test_preference_space_transform_multiple():
    """Test case 3: Multiple users and items."""
    preference_space = {
        'userA': {'item1': 'ratingA1', 'item2': 'ratingA2'},
        'userB': {'item1': 'ratingB1', 'item2': 'ratingB2'}
    }
    result = preference_space_transform(preference_space)
    expected_result = {
        'item1': {'userA': 'ratingA1', 'userB': 'ratingB1'},
        'item2': {'userA': 'ratingA2', 'userB': 'ratingB2'}
    }
    assert result == expected_result
