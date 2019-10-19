from util.commands import Commands

import pytest


def test_multiple_singleton_instantiation_failure():
    """Test that an invalid message will throw an Exception"""
    with pytest.raises(Exception) as e:
        new_singleton = Commands()
