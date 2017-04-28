# coding: utf-8
import os

class WebLib:
    def take_screenshot_on_element(self, path, driver, element):
        if not os.path.isdir(path):
            os.mkdir(path)

        filename = path+"screenshot.jpg"
        driver.save_screenshot(filename)
        left = element.location['x']
        top = element.location['y']
        right = left + element.size['width']
        bottom = top + element.size['height']
        cut_img(filename, left, top, right, bottom)

def cut_img(filename, left, top, right, bottom):
    from PIL import Image
    im = Image.open(filename)
    im = im.crop((left, top, right, bottom))
    im.save(filename)
    print "Crop Finish !!"


