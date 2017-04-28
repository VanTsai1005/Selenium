from ctypes import *

class KeyboardAndVirual:
    keyCorrespond = {}
    keyCorrespond.__setitem__("a", 401)
    keyCorrespond.__setitem__("b", 505)
    keyCorrespond.__setitem__("d", 403)
    keyCorrespond.__setitem__("c", 503)
    keyCorrespond.__setitem__("e", 303)
    keyCorrespond.__setitem__("f", 404)
    keyCorrespond.__setitem__("g", 405)
    keyCorrespond.__setitem__("h", 406)
    keyCorrespond.__setitem__("i", 308)
    keyCorrespond.__setitem__("j", 407)
    keyCorrespond.__setitem__("k", 408)
    keyCorrespond.__setitem__("l", 409)
    keyCorrespond.__setitem__("m", 507)
    keyCorrespond.__setitem__("n", 506)
    keyCorrespond.__setitem__("o", 309)
    keyCorrespond.__setitem__("p", 310)
    keyCorrespond.__setitem__("q", 301)
    keyCorrespond.__setitem__("r", 304)
    keyCorrespond.__setitem__("s", 402)
    keyCorrespond.__setitem__("t", 305)
    keyCorrespond.__setitem__("u", 307)
    keyCorrespond.__setitem__("v", 504)
    keyCorrespond.__setitem__("w", 302)
    keyCorrespond.__setitem__("x", 502)
    keyCorrespond.__setitem__("y", 306)
    keyCorrespond.__setitem__("z", 501)
    keyCorrespond.__setitem__("shift", 500)
    keyCorrespond.__setitem__("tab", 300)
    keyCorrespond.__setitem__("0", 210)
    for i in range(1, 10, 1):
        keyCorrespond.__setitem__(str(i), 200 + i)

    def passwordKeyin(self, passwd):
        dllUrl = "C:/DLL/DD64.dll"
        dd_dll = windll.LoadLibrary(dllUrl)
        for s in passwd:
            dd_dll.DD_key(int(self.keyCorrespond.__getitem__(s)), 1)
            dd_dll.DD_key(int(self.keyCorrespond.__getitem__(s)), 2)

