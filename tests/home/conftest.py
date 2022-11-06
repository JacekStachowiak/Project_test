import pytest
from selenium import webdriver
import os
from datetime import datetime


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-notifications') 
        #options.headless = True
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
        
    elif browser == 'edge':
        
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from selenium.webdriver.edge.service import Service
        from selenium.webdriver.edge.options import Options
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-notifications') 
        #options.headless = True
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    elif browser == 'firefox': 
        
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.firefox.options import Options
        options = Options()
        #options = webdriver.FirefoxOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-notifications') 
        #options.headless = True
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)               
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
        

# aby korzystać z wiersza poleceń
def pytest_addoption(parser):
    parser.addoption('--browser')    

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')   # zwraca browser do metody setup   


#### konfiguracja raportu html - 2 sposoby #########
# I dodajemy do raportu 
def pytest_configure(config):
    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester Name'] = 'JACK'

# II - usuwamy z raportu
@pytest.mark.optionalhook()
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    
# III secyfing report folder - aby nie pisać w pasku poleceń "--html=reports\report.html --capture=tee-sys"
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+"html"

