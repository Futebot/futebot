import os
from unittest.mock import MagicMock

import pytest
import unittest
from discord import File
from pytest import fail

from exception.exceptions import TooManyCharsException
from util.helpers import *
from util.validators import validate_chars_limit


class TestValidators(unittest.TestCase):

    def test_validate_chars_limit(self):
        """Test if string will be valid when under the limit"""
        try:
            validate_chars_limit("ABC", 5)
        except TooManyCharsException:
            fail("validate_chars_limit() raised TooManyCharsException unexpectedly!")

    def test_validate_chars_limit_exceeded(self):
        """Test if string will not be valid when over the limit"""
        with self.assertRaises(TooManyCharsException):
            validate_chars_limit("ABCDE", 4)
