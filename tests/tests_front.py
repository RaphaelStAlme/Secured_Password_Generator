from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
driver.get("http://localhost:4321")

time.sleep(5)

driver.close()