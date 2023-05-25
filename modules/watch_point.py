import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules import driver_browser
from config import *

def listen_portal():
    login_sv = "https://portal.vhu.edu.vn/Default.aspx?PageId=84e2e8e5-f266-4870-9a43-d1234ba033e8&ModuleID=1ab9e7da-fcf5-4031-aea9-7209f1a704cc&Role=SV"
    account = VHU_USER_NAME
    password = VHU_PASSWORD
    print("Open browser")
    driver = driver_browser.get_driver_ondemand()
    driver.get(login_sv)
    driver.maximize_window()
    driver.implicitly_wait(5)
    print("get login page success")
    driver.find_element(By.ID, "ctl09_txtUserName").send_keys(account)
    driver.find_element(By.ID, "ctl09_txtPassword").send_keys(password)
    driver.find_element(By.ID, "ctl09_btnDangnhap").click()
    
    wait = WebDriverWait(driver, 40)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "xemdiem")))
    print("login success")
    driver.find_element(By.CLASS_NAME, "xemdiem").find_element(By.TAG_NAME, "a").click()
    
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "studyprogram_tabledetails_td_content_aligncenter_dl")))
    
    time.sleep(5)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    rows = soup.find_all("tr")
    points = {}
    print("parse points")
    points["ten_sv"] = soup.find("div", {"class": "panelcontent1"}).find("div").text
    for row in rows:
        cols = row.find_all("td")
        if(len(cols) == 11):
            cols = cols[1:]
            points[cols[1].text] = cols[4].text
    del points["Tên học phần"]
    print(points)
    driver.quit()
    return points