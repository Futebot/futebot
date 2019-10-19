import re

import pytest

from service.roll_service import *


def test_roll_command():
    """Test if with the right paremeter will return a valid result"""
    response = roll("1d6")
    matches = re.findall(r"Rolled((\d)+ \+ | (\d)+ =)+ (\d)+", response)
    assert matches


def test_failed_roll_command():
    """Test that an invalid message will throw an Exception"""
    with pytest.raises(Exception) as e:
        assert roll("6")
