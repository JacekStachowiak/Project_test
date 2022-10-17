from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from base.selen_driver import SelenDriver

class LoginPage(SelenDriver):
    
    # locators
    _sing_log = '//div[contains(text(),"Sign Up or Log In")]'
    _email_field = 'email'
    _password_field = 'password'
    _login_button = '//input[@class="btn btn-default btn-block btn-md dynamic-button"]'
    _login2 = '//span[@class="caret"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def clickSingLog(self):
        self.elementClick(self._sing_log, locatorType='xpath')
    
    def enterEmailField(self, username):
        #self.getEmailField().clear()
        self.sendKeys(username, self._email_field, locatorType='id') 
    
    def enterPasswordField(self, password):
        #self.getPasswordField().clear()
        self.sendKeys(password, self._password_field, locatorType='id')               
    
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='xpath')
    
    def clicklogin2(self):
        self.elementClick(self._login2, locatorType='xpath')
                
    def loginValid(self, username, password):
        self.clickSingLog()
        self.enterEmailField(username)
        self.enterPasswordField(password)
        self.clickLoginButton()
    
    def loginSuccesfull(self, username, password):
        self.clickSingLog()
        self.enterEmailField(username)
        self.enterPasswordField(password)
        self.clickLoginButton()
        self.clicklogin2()


