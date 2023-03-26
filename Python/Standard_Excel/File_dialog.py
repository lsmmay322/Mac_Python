import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mbox
import os
import shutil


excel_ext = r"*.xlsx *.xls *.csv"

def file_find():
	file = filedialog.askopenfilenames(filetypes=(("Excel file",excel_ext), ("all file", "*.*")), \
		initialdir='/')
	en_filepath.delete(0 ,END)
	en_filepath.insert(END, file[0])

def file_upload():
	if len(en_filepath.get()) == 0:
		mbox.showinfo("warning", "select file, please")
		return
	else:
		file_name = os.path.basename(en_filepath.get())
		dest_path = os.path.join("/Users/hwanseob.lee", file_name)
		shutil.copy(en_filepath.get(), dest_path)
		en_filepath.delete(0, END)
		return

app = Tk()
en_filepath = Entry(app, width=100)
en_filepath.pack(fill="x", padx=1, pady=1)

fr_bt = Frame(app)
fr_bt.pack(fill="x", padx=1, pady=1)

bt_upload = Button(fr_bt, text="Upload", width=10, command=file_upload)
bt_upload.pack(side="right", padx=1, pady=1)
bt_find = Button(fr_bt, text="Find", width=10, command=file_find)
bt_find.pack(side="right", padx=1, pady=1)

app.title("Scribblinganything.tistory.com")
app.mainloop()


