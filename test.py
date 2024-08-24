from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tradingview.com/")
try:
    time.sleep(1)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='tv-header__user-menu-button tv-header__user-menu-button--anonymous js-header-user-menu-button']"))
    )
    element.click()
    time.sleep(1)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-name='header-user-menu-sign-in']"))
    )
    element.click()
    time.sleep(1)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email')]"))
    )
    element.click()
    time.sleep(1)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']"))
    )
    element.send_keys("m.hoo1377.ptc@gmail.com")
    time.sleep(1)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='id_password']"))
    )
    element.send_keys("@Mahdi1377Hooshmand")
    time.sleep(1)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Sign in')]"))
    )
    element.submit()
    time.sleep(1)
except:
    print("error")
finally:
    time.sleep(10)
