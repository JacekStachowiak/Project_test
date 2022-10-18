from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.register_page import RegisterPage
import unittest
from ddt import ddt, data, unpack

@ddt
class RegisterTest(unittest.TestCase):
    
    baseUrl = 'https://courses.letskodeit.com/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)
    rp = RegisterPage(driver)
    
    @data(('JavaScript for beginners', '1234 2345 3456 4567', '10/24', '345', 'Poland'), ('Learn Python 3 from scratch', '1234 2345 3456 4567', '10/24', '345', 'Poland'))
    @unpack
    def test_registerPage(self, namecourse, cardnumber, carddata, cardcode, countryname):
        self.driver.get(self.baseUrl)
        self.rp.registerCourse(namecourse)
        self.rp.card(cardnumber, carddata, cardcode) 
        self.rp.country(countryname)
                
        message = self.rp.errorCardNumber()
        assert message == 'Numer karty jest nieprawidłowy.' 
        
        # self.rp.clickAllCourse()
        
        self.driver.quit()