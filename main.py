import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create entry widget
        self.entry = tk.Entry(self.master, width=25, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        # Create buttons for numbers
        self.buttons = []
        for i in range(10):
            button = tk.Button(self.master, text=str(i), width=5, command=lambda x=i: self.button_click(x))
            self.buttons.append(button)

        # Place number buttons in grid
        for i in range(1, 10):
            row = 3 - (i - 1) // 3
            col = (i - 1) % 3
            self.buttons[i].grid(row=row, column=col)
        self.buttons[0].grid(row=4, column=0)

        # Create operator buttons
        self.add_button = tk.Button(self.master, text="+", width=5, command=lambda: self.operator_click("+"))
        self.add_button.grid(row=1, column=3)
        self.sub_button = tk.Button(self.master, text="-", width=5, command=lambda: self.operator_click("-"))
        self.sub_button.grid(row=2, column=3)
        self.mul_button = tk.Button(self.master, text="*", width=5, command=lambda: self.operator_click("*"))
        self.mul_button.grid(row=3, column=3)
        self.div_button = tk.Button(self.master, text="/", width=5, command=lambda: self.operator_click("/"))
        self.div_button.grid(row=4, column=3)

        # Create clear button
        self.clear_button = tk.Button(self.master, text="C", width=5, command=self.clear)
        self.clear_button.grid(row=4, column=1)

        # Create equal button
        self.equal_button = tk.Button(self.master, text="=", width=5, command=self.calculate)
        self.equal_button.grid(row=4, column=2)

        self.num1 = ""
        self.num2 = ""
        self.operator = ""

    def button_click(self, number):
        if self.operator == "":
            self.num1 += str(number)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.num1)
        else:
            self.num2 += str(number)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.num2)

    def operator_click(self, operator):
        self.operator = operator

    def clear(self):
        self.num1 = ""
        self.num2 = ""
        self.operator = ""
        self.entry.delete(0, tk.END)

    def calculate(self):
        if self.num1 == "" or self.num2 == "" or self.operator == "":
            return

        num1 = float(self.num1)
        num2 = float(self.num2)

        if self.operator == "+":
            result = num1 + num2
        elif self.operator == "-":
            result = num1 - num2
        elif self.operator == "*":
            result = num1 * num2
        elif self.operator == "/":
            result = num1 / num2

        self.entry.delete(0, tk.END)
        self.entry.insert(0, result)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
