# resource_l2

import os
import sys

#testdir = os.path.dirname(__file__)
#testdir = os.path.realpath(__file__)
testdir = os.getcwd()
srcdir = '../..'
src_path =  os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, os.path.abspath(src_path))

import unittest


from mhlib.l2 import l2

class TestL2(unittest.TestCase):

    def test_l2_var(self):
        self.assertEqual(l2.L2EG_VAR,'efgh')

    def test_l2_slow(self):
        x = l2.L2Mh()
        rtn = x.run()
        self.assertEqual(rtn, 10)

    def test_l2_ext(self):
        x = l2.L2Mh()
        rtn = x.slow()
        self.assertEqual(rtn, 5)


if __name__ == '__main__':
    unittest.main()