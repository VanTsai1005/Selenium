# coding:utf-8
import win32api
import win32con
import time
from ctypes import *

#  mouse_event（）有五個參數
#  第一個為行為參數
#         MOUSEEVENTF_MOVE = 0x0001; 移動滑鼠
#         MOUSEEVENTF_LEFTDOWN = 0x0002; 左鍵按下
#         MOUSEEVENTF_LEFTUP = 0x0004; 左鍵抬起
#         MOUSEEVENTF_RIGHTDOWN = 0x0008; 右鍵按下
#         MOUSEEVENTF_RIGHTUP = 0x0010; 右鍵抬起
#         MOUSEEVENTF_MIDDLEDOWN = 0x0020; 中鍵按下
#         MOUSEEVENTF_MIDDLEUP = 0x0040; 中鍵抬起
#         MOUSEEVENTF_ABSOLUTE = 0x8000; 是否用絕對座標
#  第二，三個為指定x，y方向的絕對座標或相對位置
# 第四，五不明

#  keybd_event() 有四個參數
#  第一個為按鍵的虛擬鍵值
#  第二個為掃描碼，可用"0"
# 第三個為行為參數，keydown為"0"，keyup為"KEYEVENTF_KEYUP"
# 第四個參數一般設"0"

windll.user32.SetCursorPos(1230, 380)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
time.sleep(0.5)

def input_str(ss, t):
    for i in ss:
        print i, ord(i)
        win32api.keybd_event(ord(i),0,0,0)
        win32api.keybd_event(ord(i),0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(t)

# 帳號
input_str("ABCD", 0)
win32api.keybd_event(9,0,0,0)
win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)
# 密碼
input_str("A1B2C", 5)
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)