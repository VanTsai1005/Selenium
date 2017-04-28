# coding:utf-8
from KeyboardAndVirual import passwordKeyin
from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import win32api
import win32con
import time

ACCOUNTNAME = "xxxxxxxxxxx"
PASSWORD = 'xxxxxxxxxxx'

url = "C:/tmp/code.bmp"
ie_path = "C:/IEDriverServer.exe"

def dispalyElements(state):
    js1 = "document.getElementsByClassName('header-box')[0].style.display='"+state+"';" \
          "document.getElementsByClassName('zuiai-block')[0].style.display='"+state+"';" \
          "document.getElementsByClassName('footer-block')[0].style.display='"+state+"';" \
          "document.getElementsByClassName('banner-box')[0].style.display='"+state+"';"
    js2 = "document.getElementById('includeDiv').style.display='"+state+"';" \
          "document.getElementById('shortcuttool').style.display='"+state+"';"
    web.execute_script(js1)
    web.execute_script(js2)

def displayElementFrame(state):
    js1 = "document.getElementsByClassName('wrapper-obj-left')[0].style.display='"+state+"';" \
          "for(var i=0;i<9;i++){document.getElementsByClassName('form-area-line')[i].style.display='"+state+"';}"
    js2 = "document.getElementById('registlinkdiv').style.display='"+state+"';" \
          "document.getElementsByClassName('form-area-line')[4].style.display='';"
    web.execute_script(js1)
    web.execute_script(js2)

web = webdriver.Ie(ie_path)
try:
    web.get("xxxxxxxxxxxxxxxxxxxxxxxx")
    web.maximize_window()
    dispalyElements("none")

    frame = web.find_element_by_xpath('//iframe[@name="ICBC_login_frame"]')
    web.switch_to.frame(frame)
    web.find_element_by_id("logonCardNum").click()
    displayElementFrame("none")
    web.save_screenshot(url)

    #  程式一執行產生輸入密碼介面
    win=Tk()

    # ok按鈕的事件
    def FormOK():
        global DVCODE
        DVCODE = edit_code.get()
        win.destroy()
    #帳號密碼介面設定
    win.title("Tk GUI")
    win.geometry("300x200")
    #Code
    label_code=Label(win, text="Code : ")
    edit_code=Entry(win, text="")
    label_code.grid(column=0, row=0)
    edit_code.grid(column=1, row=0, columnspan=6)
    #BUTTON-連接事件
    button_ok = Button(win, text="OK",width="10", command=FormOK)
    button_ok.grid(column=1, row=3)
    win.mainloop()

    displayElementFrame("")

    web.find_element_by_id("logonCardNum").send_keys(ACCOUNTNAME)
    web.find_element_by_id("logonCardNum").send_keys(Keys.TAB)
    passwordKeyin(PASSWORD)
    time.sleep(0.5)

    actions = ActionChains(web)
    actions.send_keys(Keys.TAB)
    actions.perform()

    passwordKeyin(DVCODE)
    web.find_element_by_id("loginBtn").click()

    # # windll.user32.SetCursorPos(1230, 440)
    # # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    # time.sleep(0.5)
finally:
    time.sleep(10)
    web.quit()

