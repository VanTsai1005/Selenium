# coding:utf-8
from Tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, filename, master = None):
        Frame.__init__(self, master) #你想要透過Frame類別傳送的參數
        self.master = master #參考到主要的小窗口，也就是tk視窗
        self.init_window()
        self.dvcode = ""
        self.filename = filename

    #初始視窗的創建
    def init_window(self):
        #改變我們主要的小窗口的標題
        self.master.title('GUI')
        #允許小窗口去取得視窗的整個空間
        self.pack(fill=BOTH, expand=1)

        # ok按鈕的事件
        def ok_event():
            self.dvcode = edit_code.get()
            self.client_exit()

        def cancel_event():
            self.client_exit()

        okButton = Button(self, text = 'OK', width="10", command=ok_event)
        okButton.place(x = 110, y = 30)
        cancelButton = Button(self, text = 'Cancel', width="10", command=cancel_event)
        cancelButton.place(x = 10, y = 30)
        label_code = Label(self, text="Code : ")
        edit_code = Entry(self, text="")
        label_code.grid(column=0, row=0)
        edit_code.grid(column=1, row=0, columnspan=6)

        # #建立一個選單實體
        # menu = Menu(self.master);
        # self.master.config(menu = menu);
        # #建立檔案物件
        # file = Menu(menu);
        # #添加一個命令到選單選項，呼叫它來離開，而命令，它在client_exit事件執行
        # file.add_command(label = 'Exit', command = self.client_exit);
        # #添加一個File到選單
        # menu.add_cascade(label = 'File', menu = file);
        # #建立檔案物件
        # edit = Menu(menu);
        # #添加一個命令到選單選項，呼叫它來離開，而命令，它在client_exit事件執行
        # edit.add_command(label = 'Undo');
        # edit.add_command(label = 'Show Img', command = self.showImg);
        # edit.add_command(label = 'Show Text', command = self.showText);
        # #添加Undo到選單
        # menu.add_cascade(label = 'Edit', menu = edit);

    def client_exit(self):
        self.master.destroy();

    def showImg(self):
        load = Image.open(self.filename);
        render = ImageTk.PhotoImage(load);
        #標籤可以是文字或圖片
        img = Label(self, image = render);
        img.image = render;
        img.place(x = 40, y = 70);  #將影像放入視窗裡

    def showText(self):
        text = Label(self, text = '成功呈現');
        text.pack();

# #視窗的建立，只會有一個，但是你可以在視窗裡建立小窗口
# root = Tk();
#
# #視窗的大小
# root.geometry('400x300');
#
# app = Window("C:/Users/use/Desktop/screenshot.jpg", root); #建立一個實體
# app.showImg()
#
# root.mainloop(); #呈現它

