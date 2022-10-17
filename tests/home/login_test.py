from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.login_page import LoginPage
from selenium.webdriver.common.by import By
import unittest

class LoginTest(unittest.TestCase):
    
    def test_validLogin(self):
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        lp = LoginPage(driver)
        lp.loginValid('test@email.com', 'abcabcABC')
        
        message_valid = lp.loginNotOK()
        assert message_valid == 'Your username or password is invalid. Please try again.'       
        
        '''
        verifyLogin = driver.find_element(By.XPATH, '//span[@class="dynamic-text help-block"]').text
        
        if verifyLogin is not None:
            print(f'Element znaleziony: {verifyLogin}')
            assert verifyLogin == 'Your username or password is invalid. Please try again.'
        else:
            print('Nie ma elementu')'''            

    def test_loginSucces(self):
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        lp = LoginPage(driver)
        lp.loginSuccesfull('test@email.com', 'abcabc')
        
        message_succes = lp.loginOK()
        assert message_succes == 'My Account'
        '''        
        loginSuccesfull = driver.find_element(By.XPATH, '//a[contains(text(),"My Account")]').text
                
        if loginSuccesfull is not None:
            print('Login succesfull')
            assert loginSuccesfull == 'My Account'
        else:
            print('Nie udało się zalogować')'''            
        
        driver.quit()

