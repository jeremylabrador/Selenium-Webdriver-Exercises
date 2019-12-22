import unittest


class TestListMethodsOne(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Running one time setUpClass")

    def setUp(self):
        print("\nRunning method level setUp")

    def test_sum(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(sum(list), 15)

    def test_pop(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(list.pop(0), 1)

    def test_reverse(self):
        list = [1, 2, 3, 4, 5]
        list.reverse()
        self.assertEqual(list, [5, 4, 3, 2, 1])

    def tearDown(self):
        print("Running method level tearDown")

    @classmethod
    def tearDownClass(cls):
        print("Running one time tearDownClass")


if __name__ == '__main__':
    unittest.main()
