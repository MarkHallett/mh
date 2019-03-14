# test_mh.py

import unittest

from mh import eg

class TestMh(unittest.TestCase):
    def test_1(self):
        print ('in test 1')
        print (dir(eg))
        r = eg.test()
        print (r)

        x = eg.Mh()
        x.runMh()


if __name__ == '__main__':
    unittest.main()
