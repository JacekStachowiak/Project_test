from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.home.register_page import RegisterPage
from pages.home.navigation_page import NavigationPage
import unittest
from ddt import ddt, data, unpack
import pytest

@ddt
class RegisterTest(unittest.TestCase):
    
    baseUrl = 'https://courses.letskodeit.com/'
    
    @data(('JavaScript for beginners', '1234 2345 3456 4567', '10/24', '345', 'Poland'),
          ('Complete Test Automation Bundle', '1234 2345 3456 4567', '10/24', '345', 'Poland'))
    
    @unpack
    @pytest.mark.run(order=1)
    def test_registerPage(self, setup, fullName, cardnumber, carddata, cardcode, countryname):
        
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.rp = RegisterPage(self.driver)
        self.rp.registerCourse(fullName)
        self.rp.card(cardnumber, carddata, cardcode) 
        self.rp.country(countryname)
        
        message = self.rp.errorCardNumber()
        assert message == 'Numer karty jest nieprawidłowy.' 
                        
        self.driver.quit()