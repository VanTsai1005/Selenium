from selenium import webdriver
import time

ie_path = "C:/IEDriverServer.exe"
chrome_path = "C:/chromedriver.exe"

ACCOUNTNAME = "xxxxxxxxxxxxxx"
def passwdKeyIn():
	char_str = "xxxxxxxxxxxxxxxxxxx"
	num_str = "xxxxxxxxxxxxxxx"


url = "C:/Users/use/Desktop/code.bmp"

WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

# web = webdriver.Ie(ie_path)
web = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)

web.get("https://wap.95559.com.cn/mobs/main.html#public/login/login")
try:
    web.maximize_window()
    time.sleep(2)
    web.find_element_by_id("login_username").send_keys(ACCOUNTNAME)
    web.find_element_by_id("login_password").click()
    passwdKeyIn();

    web.find_elements_by_class_name("ui-grid-b_3")[0].find_element_by_class_name("ui-block-c").click()
    web.find_element_by_id("login_button").click()
finally:
    time.sleep(5)
    web.quit()