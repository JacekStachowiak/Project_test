from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.login_page import LoginPage
from selenium.webdriver.common.by import By
import unittest
import pytest

class LoginTest(unittest.TestCase):
    
    @pytest.mark.run(order=1)
    def test_validLogin(self): 
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        lp = LoginPage(driver)       
        driver.get(baseUrl)
        
        lp.loginValid('test@email.com', 'abcabcABC')
        message_valid = lp.loginNotOK()
        assert message_valid == 'Your username or password is invalid. Please try again.'       
        driver.quit()
    
                 
    @pytest.mark.run(order=2)   # kolejność testów
    def test_loginSucces(self):  
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        lp = LoginPage(driver) 
        driver.get(baseUrl)
        
        lp.loginSuccesfull('test@email.com', 'abcabc')
        message_succes = lp.loginOK()
        assert message_succes == 'My Account'
        driver.quit()
    
    def test_loginPustePole(self):
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        lp = LoginPage(driver) 
        driver.get(baseUrl)
        
        lp.loginValid('test@email.com', 'abcabc')
        message_succes = lp.loginOK()
        assert message_succes == 'My Account'
        driver.quit()
        
                
        

