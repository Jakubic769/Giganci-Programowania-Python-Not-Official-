import funkcje as funkcje
import unittest

class TestAdd(unittest.TestCase):
#    def test_add(self):
#        self.assertEqual(funkcje.add(2, 4), 6)
#        self.assertNotEqual(funkcje.add(2,4), 5)

    def test_if_palindrom(self):
#        self.assertEqual(funkcje.if_palindrom("kajak"), True)
#        self.assertNotEqual(funkcje.if_palindrom("Sigma"), True)
        self.assertTrue(funkcje.if_palindrom("ala"))
        self.assertFalse(funkcje.if_palindrom("wiktor"))

if __name__ == '__main__':
    unittest.main()