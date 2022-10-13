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
    #_card_number = 'cardnumber'
    #_card_data = 'exp-date'
    #_card_code = 'cvc'
    #_country_select = 'country-list'
        
    def __init__(self, driver):
        self.driver = driver
    
    def registerCourse(self, namecourse):
        
        all_course = self.driver.find_element(By.LINK_TEXT, self._all_course)
        all_course.click()
        
        search = self.driver.find_element(By.XPATH, self._search_course)
        search.clear()
        search.send_keys(namecourse)
        button_search = self.driver.find_element(By.XPATH, self._button_search)
        button_search.click()
        
        course = self.driver.find_element(By.XPATH, self._course)
        course.click()
        button_enroll = self.driver.find_element(By.XPATH, self._button_enroll)
        button_enroll.click()
        
        self.driver.execute_script("window.scrollBy(0,700);")    
        


    def card(self, cardnumber, carddata, cardcode):
        
        card_number = self.driver.switch_to.frame(By.XPATH, self._iframe1)
        #card_number = self.driver.find_element(By.NAME, self._card_number)        
        card_number.clear()
        card_number.send_keys(cardnumber)
        time.sleep(2)
                
        card_data = self.driver.switch_to.frame(By.XPATH, self._iframe2)
        #card_data = self.driver.find_element(By.NAME, self._card_data)
        card_data.clear()
        card_data.send_keys(carddata)
        time.sleep(2)
                
        card_code = self.driver.switch_to.frame(By.XPATH, self._iframe3)
        #card_code = self.driver.find_element(By.NAME, self.card_code)
        card_code.clear()
        card_code.send_keys(cardcode)
        time.sleep(2)
    
    '''
    def country(self, countryname):
        
        country = self.driver.find_element(By.NAME, self._country_select)
        card_country = Select(country)
        card_country.select_by_visible_text(countryname)'''
