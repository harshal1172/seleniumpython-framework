import time
#py.test --show-capture=no -s -v tests/home/login_test.py --browser chrome
from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.statustest import StatusTest
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = StatusTest(self.driver)

    @pytest.mark.run(order=2)
    def test_check_validlogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_check_validlogin", result2, "Login not done")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@email.com", "test")
        result = self.lp.verifyLoginFailed()
        #assert result == False
        self.ts.mark(result, "User was not logged in with invalid")
        #//span[contains(.,'Your username or password is invalid. Please try again.')]


