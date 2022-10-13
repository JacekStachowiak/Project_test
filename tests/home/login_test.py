from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pages.home.login_page import LoginPage

class LoginTest():
    
    def test_validLogin():
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        lp = LoginPage(driver)
        lp.login('test@email.com', 'abcabc')
        
        # assert self._verify_login == 'Your username or password is invalid. Please try again.'
        driver.quit()

run_test = LoginTest()
run_test.test_validLogin()