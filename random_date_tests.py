import unittest

from random_date_service import (
    generate_random_date
)






class TestAddFunction(unittest.TestCase):
    def test_generate_date_time_1(self):
        self.assertEqual(generate_random_date(1, 2), 3)

    def test_generate_date_time_2(self):
        self.assertEqual(generate_random_date(-1, -2), -3)

    def test_generate_date_time_3(self):
        self.assertEqual(generate_random_date(1, -2), -1)

if __name__ == '__main__':
    unittest.main()