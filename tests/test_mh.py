import unittest

# Use local src for testing
import os
import sys
testdir = os.getcwd()
srcdir = '../src'
src_path =  os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, os.path.abspath(src_path))

import mh


class MhTestCase(unittest.TestCase):
    def test_var(self):
        self.assertEqual(mh.EG_VAR2, 'ABCD')

    def test_function(self):
        self.assertEqual(mh.testFunction(), 'OK')

    def test_class(self):
        my_mh = mh.Mh()
        self.assertEqual(my_mh.runMh(), 100)


if __name__ == '__main__':
    print (mh)
    print (f"{mh.__version__=}")
    unittest.main()
