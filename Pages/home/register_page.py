from email import message
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from base.selen_driver import SelenDriver
import utilities.custom_logger as cl
import logging

class RegisterPage(SelenDriver):
    
    log = cl.customLogger(logging.DEBUG)
    
#===============================
#          locators
#===============================
    _search_course = '//input[@id="search"]'
    _course = '//h4[contains(@class, "dynamic-heading") and contains(text(), "{0}")]'  #'//h4[@class="dynamic-heading"]' 
    _all_course = 'ALL COURSES'
    _courses_all = '//div[@id="course-list"]//h4[@class="dynamic-heading"'
    _button_enroll = '//button[@class="dynamic-button btn btn-default btn-lg btn-enroll"]'
    _button_search = '//button[@class="find-course search-course"]'
    _iframe1 = '//*[@id="card-number"]/div/iframe'
    _iframe2 = '//*[@id="card-expiry"]/div/iframe'
    _iframe3 = '//*[@id="card-cvc"]/div/iframe'
    _card_number = 'cardnumber'
    _card_data = 'exp-date'
    _card_code = 'cvc'
    _country_select = 'country-list'
    _error_number_card = '//div[@class="card-errors has-error"]'

        
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
   
    def clickAllCourse(self):
        self.elementClick(self._all_course, locatorType='text')     # locatorType dopisuję dla jasności kodu
    
    #def enterSearchCourse(self, namecourse):
        #self.sendKeys(namecourse, self._search_course, locatorType='xpath')       
        
    #def clickButtonSearch(self):
        #self.elementClick(self._button_search, locatorType='xpath')
    
    def selectCourse(self, fullName):
        self.elementClick(self._course.format(fullName), 'xpath')
        
    def clickCourse(self):
        self.elementClick(self._course, locatorType='xpath')
    
    def clickButtonEnroll(self):
        self.elementClick(self._button_enroll, locatorType='xpath')        
        
    def enterCardNumber(self, cardnumber):
        self.sendKeys(cardnumber, self._card_number, locatorType='name')
            
    def enterCardData(self, carddata):
        self.sendKeys(carddata, self._card_data, locatorType='name')
            
    def enterCardCode(self, cardcode):
        self.sendKeys(cardcode, self._card_code, locatorType='name')
        
   
    def selectCountry(self, countryname):
        self.select(countryname, self._country_select, locatorType='name')

    def registerCourse(self, fullName):
        self.clickAllCourse()
        #self.enterSearchCourse(namecourse)
        #self.clickButtonSearch()
        self.selectCourse(fullName)
        self.clickButtonEnroll()
        
    def card(self, cardnumber, carddata, cardcode):   
        self.webScroll('down')
        self.startFrame(self._iframe1, 'xpath')
        self.enterCardNumber(cardnumber)
        self.endFrame()
        self.startFrame(self._iframe2, 'xpath')
        self.enterCardData(carddata)
        self.endFrame()
        self.startFrame(self._iframe3, 'xpath')
        self.enterCardCode(cardcode)
        self.endFrame()
    
    def country(self, countryname):
        self.selectCountry(countryname)
    
    def errorCardNumber(self):
        result = self.getText(self._error_number_card, 'xpath')
        return result    

