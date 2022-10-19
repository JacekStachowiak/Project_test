from email import message
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.selen_driver import SelenDriver
import utilities.custom_logger as cl
import logging

class NavigationPage(SelenDriver):
    
    log = cl.customLogger(logging.DEBUG)
    
#===============================
#          locators
#===============================
    _my_courses = 'All Courses'
    _all_courses = 'My Courses'
    _user_icon = '//div[@class="dropdown"]'

        
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def navigateAllCourse(self):
        self.elementClick(self._all_courses, locatorType='text')
    
    def navigateMyCourses(self):
        self.elementClick(self._my_courses, locatorType='text')
    
    def navigateToUserIcon(self):
        self.elementClick(self._user_icon, 'xpath')
