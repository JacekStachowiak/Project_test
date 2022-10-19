from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.register_page import RegisterPage
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time

@ddt
class RegisterCSVTest(unittest.TestCase):
    
    baseUrl = 'https://courses.letskodeit.com/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseUrl)
    rp = RegisterPage(driver)
    
    @data(*getCSVData('/klon/Project_test/testdata.csv'))
    @unpack
    def test_registerPage(self, fullName, cardnumber, carddata, cardcode, countryname):
        
        self.rp.registerCourse(fullName)
        time.sleep(1)
        self.rp.card(cardnumber, carddata, cardcode) 
        time.sleep(1)
        self.rp.country(countryname)
        time.sleep(1)                
        message = self.rp.errorCardNumber()
        assert message == 'Numer karty jest nieprawidłowy.' 
                        
        self.driver.quit()