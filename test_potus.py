#!/usr/bin/env python
import unittest
import sys
from ANSWERS.president import President

class TestPresident(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.p = President(1)

    def test_pres_1_lastname_is_washington(self):
        self.assertEqual('Washington', self.p.last_name)

    def test_pres_1_firstname_is_george(self):
        self.assertEqual('George', self.p.first_name)

    @unittest.skipUnless(sys.platform == 'win32', "Only implemented on Windows")
    def test_out_of_range_terms(self):
        with self.assertRaises(ValueError):
            p = President(0)
        with self.assertRaises(ValueError):
            p = President(46)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
