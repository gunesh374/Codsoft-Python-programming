import tkinter as tk

class CalculatorApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.display = tk.Entry(self.root, width=20)
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button_text in buttons:
            if button_text == '=':
                btn = tk.Button(self.root, text=button_text, command=self.calculate)
            elif button_text == 'C':
                btn = tk.Button(self.root, text=button_text, command=self.clear_display)
            else:
                btn = tk.Button(self.root, text=button_text, command=lambda text=button_text: self.update_display(text))
            btn.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def update_display(self, value):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + value)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if _name_ == "_main_":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
