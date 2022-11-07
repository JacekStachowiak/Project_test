from pages.home.register_page import RegisterPage
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
import pytest
import time
from utilities.readProperties import ReadConfig
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@ddt
class RegisterTest(unittest.TestCase):
    
    baseURL = ReadConfig.getApplicationURL()
    
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-notifications') 
    #options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(baseURL)
               
    @data(('JavaScript for beginners', '1234 2345 3456 4567', '10/24', '345', 'Poland'),
          ('Complete Test Automation Bundle', '1234 2345 3456 4567', '10/24', '345', 'Poland'))
    
    @unpack
    @pytest.mark.run(order=1)
    
    def test_registerPage(self, fullName, cardnumber, carddata, cardcode, countryname):
        
        self.rp = RegisterPage(self.driver)        
        self.rp.registerCourse(fullName)
        time.sleep(1)
        self.rp.card(cardnumber, carddata, cardcode) 
        time.sleep(1)
        self.rp.country(countryname)
        time.sleep(1)
               
        message = self.rp.errorCardNumber()
        assert message == 'Numer karty jest nieprawidłowy.' 
        
        #self.driver.close()                
        