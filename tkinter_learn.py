from sys import path
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import END

class Application(tk.Frame):
    """file path load"""
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master 
        self.pack()
    
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class file_path_find(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master 
        self.pack()

        self.pathfinder()
        self.pathtext()
    
    def pathfinder(self):
        self.button_pathload = tk.Button(self)
        self.button_pathload["text"] = "选择文件"
        self.button_pathload.pack(side='left')
        self.button_pathload["command"] = self.pathload 
    def pathload(self):         
        var = filedialog.askopenfilename()
        self.text_path.delete(0,"end") 
        self.text_path.insert('insert',var)       
    def pathtext(self):
        self.text_path = tk.Entry(self)
        self.text_path.pack(side='right')

class date_show_excel(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master 
        self.pack()

        self.date_show_excel()

    def date_show_excel(self):
        for i in range(4):
            for j in range(3):
                label= tk.Label(self,text=1)
                label.grid(column=i,row=j)
root = tk.Tk()
root.title('my first GUI program')
root.geometry('1500x1000+500+300')

app = Application(master = root)
fpf = file_path_find(master = app)
dse = date_show_excel(master = app)

root.mainloop()