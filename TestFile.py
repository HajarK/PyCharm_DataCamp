from unittest import TestCase

class simpleOperationsTest(TestCase):
    def test_div(self):
        self.assertEqual(4 / 2, 2)

    def test_sub(self):
        self.assertEqual(7 - 3, 4)

class StringTest(TestCase):
    def test_case(self):
        self.assertTrue('Data'.isupper())
        self.assertFalse('CAMP'.isupper())
