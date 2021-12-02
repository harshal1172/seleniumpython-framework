import time

from pages.courses.register_courses_page import RegisterCoursePage
from utilities.statustest import StatusTest
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = StatusTest(self.driver)

    @pytest.mark.run(order=1)
    def test_check_invalidenroll(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnrole("JavaScript for beginners")
        self.courses.enrollCourse(num="6249 6515 5915 2326 595", exp="11 / 22", cvv="323")
        time.sleep(4)
        result = self.courses.verifyEnrollfailed()
        self.ts.markFinal("test_check_invalidenroll", result, "invalid details but test case passed")






