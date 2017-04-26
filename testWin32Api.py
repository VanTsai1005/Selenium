# coding=utf-8

import win32gui
import win32api
import win32con

def CallBack(hwnd, hwnds):
    s = win32gui.GetClassName(hwnd)
    if s == 'ATL:Edit':
        hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True

w1hd = win32gui.FindWindow('IEFrame', None)

print '%x' %w1hd

hwndChildList = {}
win32gui.EnumChildWindows(w1hd, CallBack, hwndChildList)

for k,v in hwndChildList.items():
    print '%s %x' %(k,v)

    tmpLen = win32gui.SendMessage(v, win32con.WM_GETTEXTLENGTH)+1
    buffer = '0' *50
    win32gui.SendMessage(v, win32con.WM_GETTEXT, tmpLen, buffer)

    print tmpLen
    print buffer[:tmpLen-1]
    win32gui.SendMessage(v,win32con.WM_SETTEXT,None,'test123')