import pyodbc  
import tkinter as tk
from tkinter import ttk

conn = pyodbc.connect('Driver=SQL Server;'
                      'Server=PC409;'
                      'Database=QLMonAn;'
                      'Trusted_Connection=True;')

def layNhomMonAn():
    query = "select TenNhom from NhomMonAn"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    result_list = [row[0] for row in rows]
    return result_list
    
def layMonAn():
    query = "select * from MonAn"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

layMonAn()
root = tk.Tk()
root.geometry("720x376")
root.title("Quan ly mon an")
lbl = tk.Label(root, text="Nhom mon an")
lbl.grid(row = 1, column = 1)

cbb = ttk.Combobox(root, values = layNhomMonAn())
cbb.grid(row = 1, column = 2)

columns = ("Mã Món Ăn","Tên Món Ăn","Đơn Vị Tính","Đơn Giá","Nhóm")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

style = ttk.Style()
style.configure("Treeview", rowheight=30)

tree.grid(row = 2, column = 2)

for item in layMonAn():
    tree.insert("", 'end', values = str(item))
layNhomMonAn()
root.mainloop()




