import pytest
from recommender.similarity_measure import cosine


def test_cosine_empty():
    """Test case 1: No preferences for any users."""
    preference_space = {'userA': {}, 'userB': {}}
    person1 = 'userA'
    person2 = 'userB'
    result = cosine(preference_space, person1, person2)
    assert result == 0


def test_cosine_single_no_common_items():
    """Test case 2: Two users, no common items, expect 0 similarity."""
    preference_space = {'userA': {'item1': 1}, 'userB': {'item2': 0}}
    person1 = 'userA'
    person2 = 'userB'
    result = cosine(preference_space, person1, person2)

    assert result == 0


def test_cosine_two_users_with_common_items():
    """Test case 3: Two users with common items, expect non-zero similarity."""
    preference_space = {
        'userA': {'item1': 1, 'item2': 2},
        'userB': {'item1': 1, 'item2': 1}
    }
    person1 = 'userA'
    person2 = 'userB'
    result = cosine(preference_space, person1, person2)
    assert result == 1.0
