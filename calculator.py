import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.resizable(False, False)

        self.expr = tk.StringVar()
        entry = tk.Entry(master, textvariable=self.expr, font=('Arial',16), bd=10, insertwidth=2, justify='right')
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons
        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('C',4,2), ('+',4,3),
            ('=',5,0,4)
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn)==4 else 1
            action = self.evaluate if text=='=' else (self.clear if text=='C' else lambda t=text: self.click(t))
            tk.Button(master, text=text, width=5, height=2, font=('Arial',14),
                      command=action).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

    def click(self, char):
        self.expr.set(self.expr.get() + char)

    def clear(self):
        self.expr.set("")

    def evaluate(self):
        try:
            result = eval(self.expr.get())
            self.expr.set(result)
        except Exception:
            self.expr.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
