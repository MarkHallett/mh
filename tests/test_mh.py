import unittest
import mh


class MhTestCase(unittest.TestCase):
    def test_var(self):
        self.assertEqual(mh.EG_VAR2, 'ABCD')

    def test_function(self):
        self.assertEqual(mh.test_function(), 'OK')

    def test_class(self):
        my_mh = mh.Mh()
        self.assertEqual(my_mh.run_mh(), 100)


if __name__ == '__main__':
    print(f"{mh.__version__=}")
    unittest.main()
