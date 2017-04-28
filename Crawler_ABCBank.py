from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from KeyboardAndVirual import passwordKeyin
from WebLib import WebLib
import time

ie_path = "C:/IEDriverServer.exe"
path = "C:/tmp/"
web = webdriver.Ie(ie_path)

ACCOUNTNAME = "xxxxxxxxxxxxxx"
PASSWORD = "xxxxxxxxxxxxxxx"
try:
    web.get("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    web.find_element_by_id("img2")

    web.find_element_by_id("UserBox").clear()
    web.find_element_by_id("UserBox").send_keys(ACCOUNTNAME)
    web.find_element_by_id("UserBox").send_keys(Keys.TAB)
    passwordKeyin(PASSWORD)
    img = web.find_element_by_id("img2")
    web_crop = WebLib()
    web_crop.take_screenshot_on_element(path, web, img)
finally:
    time.sleep(10)
    web.quit()