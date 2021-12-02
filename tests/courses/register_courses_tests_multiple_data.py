import time

from pages.courses.register_courses_page import RegisterCoursePage
from utilities.statustest import StatusTest
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = StatusTest(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "6249 6515 5915 2326 595", "11 / 22", "323"),("JavaScript for beginners", "6249 6515 5915 2326 595", "11 / 22", "323"))
    @unpack
    def test_check_invalidenroll(self, coursename, ccNum, ccExp, ccCvv):
        self.courses.enterCourseName(coursename)
        self.courses.selectCourseToEnrole(coursename)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCvv)
        time.sleep(4)
        result = self.courses.verifyEnrollfailed()
        self.ts.markFinal("test_check_invalidenroll", result, "invalid details but test case passed")
        self.courses.clickAllCourses()






