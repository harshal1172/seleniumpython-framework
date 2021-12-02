import time

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class RegisterCoursePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locator
    _all_courses = "//a[normalize-space()='ALL COURSES']"
    _search_box = "search"
    _search_boxkeys = "//input[@id='search']"
    _search_button = "//button[@type='submit']"
    _course = "//h4[normalize-space()='{0}']"
    _enroll_button = "//button[normalize-space()='Enroll in Course']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"
    _cc__vv = "cvc"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _enroll_error_message = "//span[normalize-space()='Your card number is invalid.']"

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_boxkeys, locatorType='xpath')

    def selectCourseToEnrole(self, fullcoursename):
        self.elementClick(locator=self._course.format(fullcoursename), locatorType="xpath" )

    def clickEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def clickAllCourses(self):
        self.elementClick(self._all_courses, locatorType="xpath")

    #def clickSearchBox(self):
        #self.elementClick(self._search_box, locatorType="name")

    def enterCardNumber(self, num):
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeys(num, self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterexpdate(self, expdate=""):
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(expdate, self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def entercvv(self, cvv=""):
        self.SwitchFrameByIndex(self._cc__vv, locatorType="name")
        self.sendKeys(cvv, self._cc__vv, locatorType="name")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enterCardInformation(self, num, exp, cvv):
        print(num)
        self.enterCardNumber(num)
        self.enterexpdate(exp)
        self.entercvv(cvv)

    def enrollCourse(self, num="",exp="",cvv=""):
        self.clickEnrollButton()
        #self.webScroll(direction="down")
        self.driver.execute_script("window.scrollBy(0, 800);")
        self.enterCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollfailed(self):
        result = self.isElementDisplayed(locator=self._enroll_error_message, locatorType="xpath")
        return result



