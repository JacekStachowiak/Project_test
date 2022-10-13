from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select


# locators
_all_course = 'ALL COURSES'
_search_course = '//input[@id="search"]'




class RegisterCourse():
    
    def test_register(self):
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
    

        all_course = driver.find_element(By.LINK_TEXT, 'ALL COURSES')
        all_course.click()
        search = driver.find_element(By.XPATH, '//input[@id="search"]')
        search.clear()
        search.send_keys('JavaScript')
        button_search = driver.find_element(By.XPATH, '//button[@class="find-course search-course"]')
        button_search.click()
        course = driver.find_element(By.XPATH, '//h4[@class="dynamic-heading"]')
        course.click()
        button_enroll = driver.find_element(By.XPATH, '//button[@class="dynamic-button btn btn-default btn-lg btn-enroll"]')
        button_enroll.click()

        driver.execute_script("window.scrollBy(0,700);")    # poziom i drugi: zakres dokąd
                
        driver.switch_to.frame(0)
        
        card_number = driver.find_element(By.NAME, 'cardnumber')        
        card_number.clear()
        card_number.send_keys('1234 2345 3456 4567')
        
        _errorLocator = '//h3[contains(@class, "dynamic-heading") and contains(text(), "{0}" )]'
        _errorElement = _errorLocator.format('Numer karty jest nieprawidłowy.')
        error = driver.find_element(By.XPATH, _errorElement) 
        
        assert error == 'Numer karty jest nieprawidłowy.'
        
        '''
        card_data = driver.find_element(By.NAME, 'exp-date')
        card_data.clear()
        card_data.send_keys('10/23')
        
        card_code = driver.find_element(By.NAME, 'cvc')
        card_code.clear()
        card_code.send_keys('345')
        
        country = driver.find_element(By.NAME, 'country-list')
        card_country = Select(country)
        card_country.select_by_visible_text('Poland')
        '''
        driver.quit()
        
run_test = RegisterCourse()
run_test.test_register()        
        