import tkinter as tk
from tkinter import ttk, messagebox

class WindowsCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Windows Calculator")
        master.configure(bg="#000000")  # Light gray background

        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.expression = ""

        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Segoe UI', 20), background="#000000", borderwidth=0)
        style.configure("TLabel", padding=10, font=('Segoe UI', 16), background="#000000", anchor="e")
        style.configure("Result.TLabel", padding=20, font=('Segoe UI', 24, "bold"), background="#000000", anchor="e")

        # Result display
        result_label = ttk.Label(master, textvariable=self.result_var, style="Result.TLabel")
        result_label.grid(row=0, column=0, columnspan=4, sticky="ew")

        # Button grid
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("+/-", 5, 1), ("%", 5, 2), ("√",5,3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(master, text=text, command=lambda t=text: self.on_button_click(t), style="TButton")
            button.grid(row=row, column=col, sticky="nsew")
            master.grid_columnconfigure(col, weight=1)
            master.grid_rowconfigure(row, weight=1)

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_columnconfigure(3, weight=1)

    def on_button_click(self, text):
        if text == "C":
            self.result_var.set("0")
            self.expression = ""
        elif text == "=":
            try:
                result = eval(self.expression)
                self.result_var.set(str(result))
                self.expression = str(result)
            except Exception as e:
                self.result_var.set("Error")
                self.expression = ""
        elif text == "+/-":
            try:
                current = float(self.result_var.get())
                self.result_var.set(str(-current))
                self.expression = str(-current)
            except ValueError:
                self.result_var.set("Error")
                self.expression = ""
        elif text == "%":
            try:
                 current = float(self.result_var.get())
                 self.result_var.set(str(current/100))
                 self.expression = str(current/100)
            except ValueError:
                self.result_var.set("Error")
                self.expression = ""
        elif text == "√":
            try:
                current = float(self.result_var.get())
                if current < 0:
                    self.result_var.set("Error")
                    self.expression = ""
                else:
                    self.result_var.set(str(current**0.5))
                    self.expression = str(current**0.5)
            except ValueError:
                self.result_var.set("Error")
                self.expression = ""
        else:
            if self.result_var.get() == "0":
                self.result_var.set(text)
                self.expression = text
            else:
                self.result_var.set(self.result_var.get() + text)
                self.expression += text

root = tk.Tk()
calculator = WindowsCalculator(root)
root.mainloop()                                 