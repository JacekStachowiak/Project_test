from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.login_page import LoginPage
from selenium.webdriver.common.by import By
import unittest
import pytest

class LoginTest(unittest.TestCase):
    
    baseUrl = 'https://letskodeit.com/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseUrl)
    lp = LoginPage(driver)
    
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        
        self.lp.loginValid('test@email.com', 'abcabcABC')
        message_valid = self.lp.loginNotOK()
        assert message_valid == 'Your username or password is invalid. Please try again.'       
        self.driver.quit()
                 
    @pytest.mark.run(order=1)   # kolejność testów
    def test_loginSucces(self):
        
        self.lp.loginSuccesfull('test@email.com', 'abcabc')
        message_succes = self.lp.loginOK()
        assert message_succes == 'My Account'
        #self.driver.quit()

