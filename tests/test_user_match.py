import pytest
from recommender.similar_item import user_match


def test_user_match_empty():
    """Test case 1: Empty preference_space."""
    preference_space = {}
    person_to_recommend = 'userA'
    result = user_match(preference_space, person_to_recommend)
    print(result)
    assert result == []


def test_user_match_single_no_match():
    """Test case 2: One user, no match."""
    preference_space = {'userA': {'item1': 'ratingA1'}}
    person_to_recommend = 'userA'
    result = user_match(preference_space, person_to_recommend)
    assert result == []
