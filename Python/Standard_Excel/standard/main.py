from tkinter import *
from tkinter import filedialog

def domenu():
    print("OK")

def open():
    filename = filedialog.askopenfilenames(initialdir="/", title="Select File",
                                            filetypes= (("Excel File", ("*csv", "*.xlsx")), ("all File", "*.*")))
    print(filename)

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=domenu)
filemenu.add_command(label="Open", command=open)
filemenu.add_command(label="Save", command=domenu)
filemenu.add_command(label="Save as...", command=domenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=domenu)
editmenu.add_command(label="Paste", command=domenu)
editmenu.add_separator()
editmenu.add_command(label="Delete", command=domenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=domenu)

root.config(menu=menubar)
root.mainloop()