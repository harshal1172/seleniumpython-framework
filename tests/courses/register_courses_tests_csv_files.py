import time

from pages.courses.register_courses_page import RegisterCoursePage
from utilities.statustest import StatusTest
from pages.home.navigation_page import NavigationPage
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegistermultipleCourseTestCSVdata(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = StatusTest(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/home/harshal/PycharmProjects/letskodeframework/testdata.csv"))
    @unpack
    def test_check_invalidenroll(self, coursename, ccNum, ccExp, ccCvv):
        self.courses.enterCourseName(coursename)
        self.courses.selectCourseToEnrole(coursename)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCvv)
        time.sleep(4)
        result = self.courses.verifyEnrollfailed()
        self.ts.markFinal("test_check_invalidenroll", result, "invalid details but test case passed")
        self.nav.navigateToAllCourses()






