import unittest

from mhlib import eg, l2


class MhTestCase(unittest.TestCase):
    def test_internal_func(self):
        my_x = eg.MhEg()
        self.assertEqual(my_x.call_external_func(), 5)

    def test_internal_func2(self):
        my_x = eg.MhEg()
        self.assertEqual(my_x.run_mh_eg(), 10)

    def test_internal_func3(self):
        my_x = eg.MhEg()
        self.assertEqual(my_x.slow(), None)


class TestTestFunction(unittest.TestCase):
    def test_internal_func(self):
        self.assertEqual(eg.test(), 'ok1')


class TestL2(unittest.TestCase):
    def test_internal_func(self):
        self.assertEqual(l2.l2.L2EG_VAR, 'efgh')
        self.assertEqual(l2.l2.l2_test(), 'ok2')


class TestL2Class(unittest.TestCase):
    def test_internal_func(self):
        my_l2 = l2.l2.L2Mh()
        self.assertEqual(my_l2.run(), 10)
        self.assertEqual(my_l2.slow(), 5)


if __name__ == '__main__':
    unittest.main()
