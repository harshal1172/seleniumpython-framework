import unittest
from tests.home.login_test import LoginTest
from tests.courses.register_courses_tests_csv_files import RegistermultipleCourseTestCSVdata

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegistermultipleCourseTestCSVdata)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)