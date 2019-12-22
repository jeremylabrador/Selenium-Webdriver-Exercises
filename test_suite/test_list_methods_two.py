import unittest


class TestListMethodsTwo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Running one time setUpClass")

    def setUp(self):
        print("\nRunning method level setUp")

    def test_extend(self):
        list = [1, 2, 3]
        list_two = [4, 5]
        list.extend(list_two)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    def test_cpunt(self):
        list = [5, 2, 5, 4, 5]
        list.count(5)
        self.assertEqual(list.count(5), 3)

    def test_len(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(len(list), 5)

    def tearDown(self):
        print("Running method level tearDown")

    @classmethod
    def tearDownClass(cls):
        print("Running one time tearDownClass")


if __name__ == '__main__':
    unittest.main()
