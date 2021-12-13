from tkinter import *
from tkinter import filedialog

class Application(Frame):
    """file path load"""

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master 
        self.pack()

        self.pathfinder()
    
    def pathfinder(self):
        self.button_pathload = Button(self)
        self.button_pathload["text"] = "选择文件"
        self.button_pathload.pack()
        self.button_pathload["command"] = self.pathload 
    def pathload(self):         
        filedialog.askdirectory()

root = Tk()
root.title('my first GUI program')
root.geometry('1500x1000+500+300')

app = Application(master = root)

root.mainloop()