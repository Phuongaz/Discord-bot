from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Remote
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options as ChromeOptions
from config import *

def get_driver_ondemand():
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 11'
    sauce_options = {}
    sauce_options['username'] = 'oauth-nnnguyentanphuong-e53de'
    sauce_options['accessKey'] = '3e3bbdcc-1fdb-47c3-90fa-9d54ff7908af'
    sauce_options['build'] = 'selenium-build-XDOA9'
    sauce_options['name'] = 'dc bot test'

    options.set_capability('sauce:options', sauce_options)

    url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)
    
    return driver

def get_driver():
    path = PATH_CHROME_DRIVER
    service_obj = Service(path)
    driver = webdriver.Chrome(service=service_obj)
    return driver