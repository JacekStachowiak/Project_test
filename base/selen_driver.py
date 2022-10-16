from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import * 
from selenium.webdriver.support.select import Select

class SelenDriver():
    
    def __init__(self, driver):
        self.driver = driver
    
    def getByType(self, locatorType):        # def dla By.ID i By.Xpath
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'text':
            return By.LINK_TEXT
        else:
            print(f'Ten typ locatora {locatorType} nie jest wspierany/nie jest dobry')
        return False            

    def getElement(self, locator, locatorType='id'):    # locator 'name', locatorType 'id'
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator) 
            print('Element Found')           
        except:
            print('Element not found')
        return element            

    def startFrame(self, locator, locatorType = 'id'):
        try:
            frame = self.getElement(locator, locatorType)
            element = self.driver.switch_to.frame(frame)
            print('Start Frame - found')
        except:
            print('Start Frame not found')  
        return element   
    
    def endFrame(self):
        element = self.driver.switch_to.default_content()
        return element 

    def select(self, countryname, locator, locatorType='id'):
        element = self.getElement(locator, locatorType)
        element2 = Select(element)
        element2.select_by_visible_text(countryname)
    
    def elementClick(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print(f'Cliked on the element with locator: {locator}, locatorType: {locatorType}')
        except:
            print(f'Cannot clik on the element with locator: {locator}, locatorType: {locatorType}')
            print_stack()
    
    def sendKeys(self, data, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print(f'Send data on  element with locator: {locator}, locatorType: {locatorType}')
        except:
            print(f'Cannot send data on the element with locator: {locator}, locatorType: {locatorType}')
            print_stack()
    
            
# aby sprawdzić czy element jest obecny na stronie - czy będzie false czy True cały czas testujemy (nie wyrzuci)
    def isElementPresent(self, byType, locator):
        try:
            element = self.driver.find_element(byType, locator) # By.Id, 'name'
            if element is not None:
                print('Element Found')
                return True
            else: 
                print('Element not found')
                return False
        except:
            print('Element not found')
            return False
    
    # drugi sposób na obecność elementu
    def isElementCheck(self, byType, locator):
        try:
            elementList = self.driver.find_elements(byType, locator) # By.Id, 'name'
            if len(elementList) > 0:
                print('Element Found')
                return True
            else:
                print('Element not found')
                return False
        except:
            print('Element not found')
            return False


    def waitForElement(self, locator, locatorType = 'id',timeout_1=10, pollFrequency_1=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print(f'Waiting for maximum:: {timeout_1} :: second for element to be visible')
            wait = WebDriverWait(self.driver, timeout=timeout_1, poll_frequency=pollFrequency_1, ignored_exceptions=[
                                                                                        NoSuchElementException,
                                                                                        ElementNotVisibleException,
                                                                                        ElementNotSelectableException ]) 
            element = wait.until(EC.visibility_of_element_located((byType, locator))) # uwaga na ilośc nawiasów
            print('Element appeared (pojawił się) on the web page')
        except:
            print('Element not appeared on the page')
            print_stack()  # ślad stosu
        return element           
        
        