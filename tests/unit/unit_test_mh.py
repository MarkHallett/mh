# unit_test_mh.py

import os
import sys

testdir = os.getcwd()
srcdir = '../..'
src_path =  os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, os.path.abspath(src_path))


import unittest
import mh

class TestMh(unittest.TestCase):
    def test_var(self):
         self.assertEqual(mh.EG_VAR2, 'ABCD_mh')

    def test_func(self):
        self.assertEqual(mh.testFunction(), 'OK')

    def test_class(self):
        x = mh.Mh()
        x.runMh()

if __name__ == '__main__':
    unittest.main()
