from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage():
    
    # locators
    _sing_log = '//div[contains(text(),"Sign Up or Log In")]'
    _email_field = 'email'
    _password_field = 'password'
    _login_button = '//input[@class="btn btn-default btn-block btn-md dynamic-button"]'

    def __init__(self, driver):
        self.driver = driver
        
    def getSingLog(self):
        return self.driver.find_element(By.XPATH, self._sing_log)
    
    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)
    
    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)
    
    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)
    
        
    def clickSingLog(self):
        self.getSingLog().click()
    
    def enterEmailField(self, username):
        self.getEmailField().clear()
        self.getEmailField().send_keys(username) 
    
    def enterPasswordField(self, password):
        self.getPasswordField().clear()
        self.getPasswordField().send_keys(password)               
    
    def clickLoginButton(self):
        self.getLoginButton().click()
        
    def login(self, username, password):
        self.getSingLog()
        self.clickSingLog()
        self.getEmailField()
        self.enterEmailField(username)
        self.getPasswordField()
        self.enterPasswordField(password)
        self.getLoginButton()
        self.clickLoginButton()
        
        

