#!/usr/bin/env python
#
import unittest
from unittest.mock import Mock
from spam import Spam

RETURN_VALUE = 99

ham = Mock(return_value=RETURN_VALUE)  # <1>


# dependency to be mocked -- not used in test
# def ham():
#     return 42

class TestSpam(unittest.TestCase):  # <5>

    def test_whatever(self):
        spam = Spam()  # <6>
        print("spam value is", spam.value)
        self.assertEqual(RETURN_VALUE, spam.value, "value is not {}".format(RETURN_VALUE))  # <7>


if __name__ == '__main__':
    unittest.main()
