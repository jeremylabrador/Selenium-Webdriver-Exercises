import unittest
from test_list_methods_one import TestListMethodsOne
from test_list_methods_two import TestListMethodsTwo

tlm1 = unittest.TestLoader().loadTestsFromTestCase(TestListMethodsOne)
tlm2 = unittest.TestLoader().loadTestsFromTestCase(TestListMethodsTwo)

suite = unittest.TestSuite([tlm1, tlm2])

unittest.TextTestRunner(verbosity=2).run(suite)
