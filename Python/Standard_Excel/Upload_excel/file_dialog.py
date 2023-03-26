from tkinter import *
from tkinter import filedialog

excel_ext = r"*.xlsx *.xls *.csv"

def file_open():
	file_dir = filedialog.askopenfilenames(title = "파일을 선택하세요", \
		filetypes=(("Excel File", excel_ext), ("all types", "*.*")), \
			initialdir="/Users/hwanseob.lee")
	return file_dir

def file_save(file_path=None):
	if file_path == None:
		file_save = filedialog.asksaveasfilename(
			filetypes= (("Excel File", excel_ext), ("all types", "*.*"))
			)
