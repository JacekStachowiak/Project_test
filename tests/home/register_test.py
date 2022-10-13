from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from pages.home.register_page import RegisterPage

class RegisterTest():
    
    def test_registerPage(self):
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        rp = RegisterPage(driver)
        rp.registerCourse('JavaScript')
        rp.card('1234 2345 3456 4567', '10/23', '345')    
        rp.country('Poland')
        
        _errorLocator = '//h3[contains(@class, "dynamic-heading") and contains(text(), "{0}" )]'
        _errorElement = _errorLocator.format('Numer karty jest nieprawidłowy.')
        error = self.driver.find_element(By.XPATH, _errorElement) 
        
        assert error == 'Numer karty jest nieprawidłowy.'
            
        driver.quit()
        
run_test = RegisterTest()
run_test.test_registerPage()        
        