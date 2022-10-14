from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class RegisterPage():
    
    # locators
    _all_course = 'ALL COURSES'
    _search_course = '//input[@id="search"]'
    _button_search = '//button[@class="find-course search-course"]'
    _course = '//h4[@class="dynamic-heading"]'
    _button_enroll = '//button[@class="dynamic-button btn btn-default btn-lg btn-enroll"]'
    _iframe1 = '//*[@id="card-number"]/div/iframe'
    _iframe2 = '//*[@id="card-expiry"]/div/iframe'
    _iframe3 = '//*[@id="card-cvc"]/div/iframe'
    _card_number = 'cardnumber'
    _card_data = 'exp-date'
    _card_code = 'cvc'
    _country_select = 'country-list'
        
    def __init__(self, driver):
        self.driver = driver
    
    
    def getAllCourse(self):
        return self.driver.find_element(By.LINK_TEXT, self._all_course)
    
    def getSearchCourse(self):
        return self.driver.find_element(By.XPATH, self._search_course)
    
    def getButtonSearch(self):
        return self.driver.find_element(By.XPATH, self._button_search)
    
    def getCourse(self):
        return self.driver.find_element(By.XPATH, self._course) 
    
    def getButtonEnroll(self):
        return self.driver.find_element(By.XPATH, self._button_enroll)
    
    def clickAllCourse(self):
        self.getAllCourse().click()
    
    def enterSearchCourse(self, namecourse):
        self.getSearchCourse().clear()
        self.getSearchCourse().send_keys(namecourse)        
    
    def clickButtonSearch(self):
        self.getButtonSearch()
    
    def clickCourse(self):
        self.getCourse().click()
    
    def clickButtonEnroll(self):
        self.getButtonEnroll().click()            
    
    def scrollWindow(self):
        return self.driver.execute_script("window.scrollBy(0,700);")
    
    def getCardNumber(self):
        return self.driver.find_element(By.NAME, self._card_number)
    
    def getCardData(self):
        return self.driver.find_element(By.NAME, self._card_data)
    
    def getCardCode(self):
        return self.driver.find_element(By.NAME, self._card_code)
    
    
    def enterCardNumber(self, cardnumber):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self._iframe1))
        self.getCardNumber().clear()
        self.getCardNumber().send_keys(cardnumber)
        self.driver.switch_to.default_content()
        time.sleep(2)
    
    def enterCardData(self, carddata):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,self._iframe2))
        self.getCardData().clear()
        self.getCardData().send_keys(carddata)
        self.driver.switch_to.default_content()
        time.sleep(2)
    
    def enterCardCode(self, cardcode):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,self._iframe3))
        self.getCardCode().clear()
        self.getCardCode().send_keys(cardcode)
        self.driver.switch_to.default_content()
        time.sleep(2)
    
    def getCountrySelect(self):
        return self.driver.find_element(By.NAME, self._country_select)
    
    def selectCountry(self, countryname):
        self.getCountrySelect()
        self.card_country = Select(self.getCountrySelect())
        self.card_country.select_by_visible_text(countryname)
    
    def registerCourse(self, namecourse):
        self.getAllCourse()
        self.clickAllCourse()
        self.getSearchCourse()
        self.enterSearchCourse(namecourse)
        self.getButtonSearch()
        self.clickButtonSearch()
        self.getCourse()
        self.clickCourse()
        self.getButtonEnroll()
        self.clickButtonEnroll()
        
    def card(self, cardnumber, carddata, cardcode):   
        self.scrollWindow()
        self.getCardNumber()
        self.enterCardNumber(cardnumber)
        self.getCardData()
        self.enterCardData(carddata)
        self.getCardCode()
        self.enterCardCode(cardcode)

    def country(self, countryname):
        self.selectCountry(countryname)
    
    
    
        #all_course = self.driver.find_element(By.LINK_TEXT, self._all_course)
        #all_course.click()
        #search = self.driver.find_element(By.XPATH, self._search_course)
        #search.clear()
        #search.send_keys(namecourse)
        #button_search = self.driver.find_element(By.XPATH, self._button_search)
        #button_search.click()
        #course = self.driver.find_element(By.XPATH, self._course)
        #course.click()
        #button_enroll = self.driver.find_element(By.XPATH, self._button_enroll)
        #button_enroll.click()

        #card_number = self.driver.find_element(By.NAME, self._card_number)        
        #card_number.clear()
        #card_number.send_keys(cardnumber)
        #card_data = self.driver.find_element(By.NAME, self._card_data)
        #card_data.clear()
        #card_data.send_keys(carddata)
        #card_code = self.driver.find_element(By.NAME, self._card_code)
        #card_code.clear()
        #card_code.send_keys(cardcode)
       
        #country = self.driver.find_element(By.NAME, self._country_select)
        #card_country = Select(country)
        #card_country.select_by_visible_text(countryname)
