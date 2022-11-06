from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.home.register_page import RegisterPage
from pages.home.navigation_page import NavigationPage
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time

#@pytest.mark.usefixtures('setUp')
@ddt
class RegisterCSVTest(unittest.TestCase):
    
    
    baseUrl = 'https://courses.letskodeit.com/'
       
    @data(*getCSVData('/klon/Project_test/testdata.csv'))
    @unpack
    def test_registerPage(self, setup, fullName, cardnumber, carddata, cardcode, countryname):
        
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.rp = RegisterPage(self.driver)
        self.rp.registerCourse(fullName)
        time.sleep(1)
        self.rp.card(cardnumber, carddata, cardcode) 
        time.sleep(1)
        self.rp.country(countryname)
        time.sleep(1)                
        message = self.rp.errorCardNumber()
        assert message == 'Numer karty jest nieprawidłowy.' 
                        
        self.driver.quit()