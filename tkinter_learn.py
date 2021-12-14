import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    """file path load"""

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
        self.text_path.insert('insert',var) 
    def pathtext(self):
        self.text_path = tk.Entry(self)
        self.text_path.pack(side='right')

root = tk.Tk()
root.title('my first GUI program')
root.geometry('1500x1000+500+300')

app = Application(master = root)

root.mainloop()