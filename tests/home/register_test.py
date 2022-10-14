from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from pages.home.register_page import RegisterPage
import unittest

class RegisterTest(unittest.TestCase):
    
    def test_registerPage(self):
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        rp = RegisterPage(driver)
        rp.registerCourse('JavaScript')
        rp.card('1234 2345 3456 4567', '10/24', '345') 
        #rp.country('Poland')
        
        
        _error = '//div[@class="card-errors has-error"]//span[text()="Numer karty jest nieprawidłowy."]'
        error_card = driver.find_element(By.XPATH, _error).text
        
        if error_card is not None:
            print(f'Element znaleziony: {error_card}')
            assert error_card == 'Numer karty jest nieprawidłowy.'
        else:
            print('Brak elementu')            
            
        driver.quit()
