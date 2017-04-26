#coding:utf-8
from DecodeVerificationCode import getVerificationCode
from selenium import webdriver
from Tkinter import *

def controlElement(status):
    js_login = "document.getElementById('{}').style.display='{}'"
    js_other = "document.getElementsByTagName('a')[{}].style.display='{}'"
    web.execute_script(js_login.format("Source", status))
    web.execute_script(js_login.format("UserName", status))
    web.execute_script(js_login.format("Password", status))
    web.execute_script(js_login.format("txtCode", status))
    web.execute_script(js_login.format("OK", status))
    web.execute_script(js_other.format("0", status))
    web.execute_script(js_other.format("1", status))

#  程式一執行產生輸入帳號密碼介面
win=Tk()
#全域帳號、密碼、THREAD數
USER_NAME = None
PASSWD = None
NUM_THREADS = None

# cancel按鈕的事件
def FormClose():
    global USER_NAME
    USER_NAME = ""
    global PASSWD
    PASSWD = ""
    win.destroy()
    exit()
# ok按鈕的事件
def FormOK():
    global USER_NAME
    USER_NAME = edit_user.get()
    global PASSWD
    PASSWD = edit_password.get()
    global NUM_THREADS
    NUM_THREADS = int(edit_thread.get())
    win.destroy()
#帳號密碼介面設定
win.title("Tk GUI")
win.geometry("300x200")
    #USER
label_user=Label(win, text="User : ")
edit_user=Entry(win, text="")
label_user.grid(column=0, row=0)
edit_user.grid(column=1, row=0, columnspan=6)
    #PASSWORD
label_password=Label(win, text="Password : ")
edit_password=Entry(win, text="", show="*")
label_password.grid(column=0, row=1)
edit_password.grid(column=1, row=1, columnspan=6)
    #Thread Num
label_thread=Label(win, text="Thread Number : ")
edit_thread=Entry(win)
edit_thread.insert(END, '1')
label_thread.grid(column=0, row=2)
edit_thread.grid(column=1, row=2, columnspan=6)
    #BUTTON-連接事件
button_cancel = Button(win, text="Cancel",  width="10", command=FormClose)
button_ok = Button(win, text="OK",width="10", command=FormOK)
button_cancel.grid(column=0, row=3)
button_ok.grid(column=1, row=3)
win.mainloop()

if USER_NAME == None or PASSWD == None:
    exit()

# phantom_path = "C:/Users/use/Anaconda2/Lib/site-packages/phantomjs-2.1.1-windows/bin/phantomjs.exe"
# web = webdriver.PhantomJS(phantom_path)

chrome_path = "C:/chromedriver.exe"
web = webdriver.Chrome(chrome_path)

web.get("https://netbank.jihsunbank.com.tw/netbank/left.asp")

COUNT = 1
while COUNT < 4:
    #  被包在iframe裡面，必須先切換
    frame = web.find_element_by_xpath('//iframe[@name="loginFrame"]')
    web.switch_to.frame(frame)

    web.find_element_by_id("UserName").send_keys(USER_NAME)
    web.find_element_by_id("Password").send_keys(PASSWD)

    #  消除不需要的元素後存成圖片
    controlElement("None")
    src = web.find_element_by_id("imgCode").get_attribute("src")+".bmp"

    url = "C:/Users/use/Desktop/code.bmp"
    web.save_screenshot(url)

    #  回復網頁上的元素進行資料填寫
    controlElement("")

    #  驗證碼辨識
    DVCODE = getVerificationCode(url)

    web.find_element_by_id("txtCode").send_keys(DVCODE)
    web.find_element_by_id("OK").click()

    #  如果辨識失敗，再重複
    try:
        if web.find_element_by_id("cmdClose"):
            web.get("https://netbank.jihsunbank.com.tw/netbank/left.asp")
            COUNT += 1
    except:
        break

if COUNT==4:
    print "Not Success !!"
    web.quit()
else:
    print "Finish !!!"