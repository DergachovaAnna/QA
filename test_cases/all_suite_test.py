import unittest
from test_cases.adding_player import TestAddPlayer
from test_cases.login_to_the_system import TestLoginPage



def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest((unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)))
   test_suite.addTest((unittest.TestLoader().loadTestsFromTestCase(TestAddPlayer)))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())