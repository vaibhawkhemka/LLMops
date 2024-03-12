import unittest

class Test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,4]),6,"Should be 6")
# def test_sum():
#     assert sum([1,2]) ==6

if __name__ == "__main__":
    unittest.main()