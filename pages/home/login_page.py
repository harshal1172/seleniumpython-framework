import time
#from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)

    #locator
    _login_link = "//a[.='Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"
    _all_courses = "//a[normalize-space()='ALL COURSES']"
    _logout = "a[href='/logout']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)
        #self.getEmail().send_keys(email)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
        #self.getPassword().send_keys(password)

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="xpath")
        #self.getLoginButton().click()

    def clickAllCourses(self):
        self.elementClick(self._all_courses, locatorType="xpath")
        #self.getAllCourses().click()

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearfields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(4)
        self.clickAllCourses()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[contains(@class,'zl-navbar-rhs-img')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//img[contains(@class,'zl-navbar-rhs-img')]", locatorType="xpath")
        return result

    def clearfields(self):
        emailfield = self.getElement(self._email_field)
        emailfield.clear()
        passwordfield = self.getElement(self._password_field)
        passwordfield.clear()

    def verifyTitle(self):
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.nav.navigateToUserSettings()
        self.elementClick(locator="(//a[normalize-space()='Logout'])[1]",locatorType="xpath")

