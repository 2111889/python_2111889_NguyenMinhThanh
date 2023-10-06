import tkinter as tk
from tkinter import Entry, Button, StringVar

class Calculator(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.expression = ""
        self.initUI()

    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = total
        except:
            self.equation.set("Error")
            self.expression = ""

    def Back(self):
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)

    def clear(self):
        self.expression = ""
        self.equation.set("")
        
    def Close(self):
        root.quit()

    def initUI(self):
        self.parent.title("Simple Calculator")

        self.grid(columnspan=4)

        self.equation = StringVar()
        expression_field = Entry(self, textvariable=self.equation)
        expression_field.grid(columnspan=4, ipadx=70)

        button_labels = [
            '.', 'Back', '', '',
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            '0', '.', '=', '/'
        ]

        row_val = 2
        col_val = 0

        for button_label in button_labels:
            Button(self, text=button_label,  command=lambda label=button_label: self.press(label), height=1, width=7).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        Button(self, text='Close',  command=self.Close, height=1, width=7).grid(row=2, column=3)
        Button(self, text='Cls',  command=self.clear, height=1, width=7).grid(row=2, column=0)
        Button(self, text='Back',  command=self.Back, height=1, width=7).grid(row=2, column=1)       
        Button(self, text='=',  command=self.equalpress, height=1, width=7).grid(row=6, column=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()