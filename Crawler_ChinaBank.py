#coding: utf-8

from Tkinter import *
from DecodeVerificationCode import getVerificationCode
from selenium import webdriver
import time

chrome_path = "C:/chromedriver.exe"
web = webdriver.Chrome(chrome_path)

ACCOUNTNAME = "YourAccountName"
PASSWORD = "YourPassword"
url = "C:/tmp/code.bmp"

try:
    web .get("https://ebsnew.boc.cn/boc15/login.html?locale=zh_CN")
    web.find_element_by_id("txt_username_79443").send_keys(ACCOUNTNAME)
    time.sleep(1)
    web.find_element_by_id("input_div_password_79445").click()
    time.sleep(2)
    web.find_element_by_id("input_div_password_79445_1").send_keys(PASSWORD)
    web.find_element_by_id("captcha_debitCard").click()

    classNames = ["bu-header", "sn-box", "login-aside", "bu-footer", "menu-tab"]
    js_hidden = "document.getElementsByClassName('{}')[0].style.display='none'"
    js1 = "document.getElementsByClassName('clearfix')[7].style.visibility='hidden'"
    js2 = "document.getElementsByClassName('clearfix')[8].style.visibility='hidden'"
    js3 = "document.getElementsByClassName('btn-login')[1].style.visibility='hidden'"
    js4 = "document.getElementsByClassName('item-title')[5].style.visibility='hidden'"
    js5 = "document.getElementById('txt_captcha_741012').style.display='none'"
    js6 = "document.getElementById('a_shuaxin_741013').style.display='none'"

    for i in range(len(classNames)):
        web.execute_script(js_hidden.format(classNames[i]))
    web.execute_script(js1)
    web.execute_script(js2)
    web.execute_script(js3)
    web.execute_script(js4)
    web.execute_script(js5)
    web.execute_script(js6)

    web.save_screenshot(url)
    #  驗證碼辨識
    DVCODE = getVerificationCode(url)

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

    js3 = "document.getElementsByClassName('btn-login')[1].style.visibility=''"
    js5 = "document.getElementById('txt_captcha_741012').style.display=''"
    web.execute_script(js3)
    web.execute_script(js5)

    web.find_element_by_id("txt_captcha_741012").send_keys(DVCODE)
    web.find_element_by_id("btn_49_741014").click()

finally:
    time.sleep(10)
    web.quit()



