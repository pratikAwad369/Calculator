# '''import tkinter as tk
# from tkinter import messagebox
# import math

# # -------------------- Calculator Logic --------------------
# class Calculator:
#     def __init__(self, entry_widget):
#         self.entry = entry_widget
#         self.reset()

#     def reset(self):
#         """Clear the display"""
#         self.entry.delete(0, tk.END)

#     def insert(self, value):
#         """Insert value into the display"""
#         self.entry.insert(tk.END, value)

#     def calculate(self):
#         """Evaluate the expression and show result"""
#         try:
#             expression = self.entry.get()
#             result = eval(expression)
#             self.reset()
#             self.insert(result)
#         except ZeroDivisionError:
#             messagebox.showerror("Error", "Division by zero is not allowed")
#             self.reset()
#         except Exception:
#             messagebox.showerror("Error", "Invalid Input")
#             self.reset()

#     def sqrt(self):
#         """Square root of current number"""
#         try:
#             value = float(self.entry.get())
#             if value < 0:
#                 raise ValueError("Negative number")
#             result = math.sqrt(value)
#             self.reset()
#             self.insert(result)
#         except Exception:
#             messagebox.showerror("Error", "Invalid Input for √")
#             self.reset()

#     def percent(self):
#         """Convert current value to percentage"""
#         try:
#             value = float(self.entry.get())
#             result = value / 100
#             self.reset()
#             self.insert(result)
#         except Exception:
#             messagebox.showerror("Error", "Invalid Input for %")
#             self.reset()

# # -------------------- GUI Setup --------------------
# def main():
#     root = tk.Tk()
#     root.title("Basic Calculator")
#     root.geometry("300x400")
#     root.resizable(False, False)

#     # Entry widget for input/output
#     entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
#     entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

#     calc = Calculator(entry)

#     # Buttons layout
#     buttons = [
#         ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
#         ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
#         ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
#         ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
#         ("C", 5, 0), ("√", 5, 1), ("%", 5, 2)
#     ]

#     for (text, row, col) in buttons:
#         action = None
#         if text == "=":
#             action = calc.calculate
#         elif text == "C":
#             action = calc.reset
#         elif text == "√":
#             action = calc.sqrt
#         elif text == "%":
#             action = calc.percent
#         else:
#             action = lambda t=text: calc.insert(t)

#         btn = tk.Button(root, text=text, font=("Arial", 14), height=2, width=5, command=action)
#         btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

#     # Make buttons responsive
#     for i in range(6):
#         root.grid_rowconfigure(i, weight=1)
#     for j in range(4):
#         root.grid_columnconfigure(j, weight=1)

#     # Keyboard input binding
#     def on_key(event):
#         if event.keysym == "Return":
#             calc.calculate()
#         elif event.keysym == "Escape":
#             calc.reset()
#         else:
#             entry.insert(tk.END, event.char)

#     root.bind("<Key>", on_key)

#     root.mainloop()

# if __name__ == "__main__":
#     main()'''
# import tkinter as tk
# from tkinter import messagebox
# import math

# # -------------------- Calculator Logic --------------------
# class Calculator:
#     def __init__(self, entry_widget):
#         self.entry = entry_widget
#         self.reset()

#     def reset(self):
#         """Clear the display"""
#         self.entry.delete(0, tk.END)

#     def insert(self, value):
#         """Insert value into the display"""
#         self.entry.insert(tk.END, value)

#     def calculate(self):
#         """Evaluate the expression and show result"""
#         try:
#             expression = self.entry.get()
#             result = eval(expression)
#             self.reset()
#             self.insert(result)
#         except ZeroDivisionError:
#             messagebox.showerror("Error", "Division by zero is not allowed")
#             self.reset()
#         except Exception:
#             messagebox.showerror("Error", "Invalid Input")
#             self.reset()

#     def sqrt(self):
#         """Square root of current number"""
#         try:
#             value = float(self.entry.get())
#             if value < 0:
#                 raise ValueError("Negative number")
#             result = math.sqrt(value)
#             self.reset()
#             self.insert(result)
#         except Exception:
#             messagebox.showerror("Error", "Invalid Input for √")
#             self.reset()

#     def percent(self):
#         """Convert current value to percentage"""
#         try:
#             value = float(self.entry.get())
#             result = value / 100
#             self.reset()
#             self.insert(result)
#         except Exception:
#             messagebox.showerror("Error", "Invalid Input for %")
#             self.reset()

# # -------------------- GUI Setup (Dark Mode) --------------------
# def main():
#     root = tk.Tk()
#     root.title("Dark Mode Calculator")
#     root.geometry("320x450")
#     root.resizable(False, False)

#     # Colors for dark mode
#     bg_color = "#2e2e2e"
#     button_color = "#3c3f41"
#     button_active = "#5c5f61"
#     text_color = "#ffffff"
#     operator_color = "#ff9500"

#     root.configure(bg=bg_color)

#     # Entry widget for input/output
#     entry = tk.Entry(root, font=("Arial", 20), borderwidth=0, relief="flat", justify="right",
#                      bg=bg_color, fg=text_color, insertbackground=text_color)
#     entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

#     calc = Calculator(entry)

#     # Buttons layout
#     buttons = [
#         ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
#         ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
#         ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
#         ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
#         ("C", 5, 0), ("√", 5, 1), ("%", 5, 2)
#     ]

#     for (text, row, col) in buttons:
#         action = None
#         if text == "=":
#             action = calc.calculate
#         elif text == "C":
#             action = calc.reset
#         elif text == "√":
#             action = calc.sqrt
#         elif text == "%":
#             action = calc.percent
#         else:
#             action = lambda t=text: calc.insert(t)

#         color = operator_color if text in ["/", "*", "-", "+", "=", "%", "√"] else button_color

#         btn = tk.Button(
#             root,
#             text=text,
#             font=("Arial", 16),
#             height=2,
#             width=5,
#             command=action,
#             bg=color,
#             fg=text_color,
#             activebackground=button_active,
#             activeforeground=text_color,
#             relief="flat",
#             bd=0
#         )
#         btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

#     # Make buttons responsive
#     for i in range(6):
#         root.grid_rowconfigure(i, weight=1)
#     for j in range(4):
#         root.grid_columnconfigure(j, weight=1)

#     # Keyboard input binding
#     def on_key(event):
#         if event.keysym == "Return":
#             calc.calculate()
#         elif event.keysym == "Escape":
#             calc.reset()
#         else:
#             entry.insert(tk.END, event.char)

#     root.bind("<Key>", on_key)

#     root.mainloop()

# if __name__ == "__main__":
#     main()
import tkinter as tk
from tkinter import messagebox
import math

# -------------------- Calculator Logic --------------------
class Calculator:
    def __init__(self, entry_widget):
        self.entry = entry_widget
        self.reset()

    def reset(self):
        """Clear the display"""
        self.entry.delete(0, tk.END)

    def insert(self, value):
        """Insert value into the display"""
        self.entry.insert(tk.END, value)

    def calculate(self):
        """Evaluate the expression and show result"""
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.reset()
            self.insert(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed")
            self.reset()
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            self.reset()

    def sqrt(self):
        """Square root of current number"""
        try:
            value = float(self.entry.get())
            if value < 0:
                raise ValueError("Negative number")
            result = math.sqrt(value)
            self.reset()
            self.insert(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input for √")
            self.reset()

    def percent(self):
        """Convert current value to percentage"""
        try:
            value = float(self.entry.get())
            result = value / 100
            self.reset()
            self.insert(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input for %")
            self.reset()

# -------------------- GUI Setup (Dark Mode) --------------------
def main():
    root = tk.Tk()
    root.title("Dark Mode Calculator")
    root.geometry("320x450")
    root.resizable(False, False)

    # Colors for dark mode
    bg_color = "#2e2e2e"
    button_color = "#3c3f41"
    button_active = "#5c5f61"
    text_color = "#ffffff"
    operator_color = "#ff9500"

    root.configure(bg=bg_color)

    # Entry widget for input/output
    entry = tk.Entry(root, font=("Arial", 20), borderwidth=0, relief="flat", justify="right",
                     bg=bg_color, fg=text_color, insertbackground=text_color)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

    calc = Calculator(entry)

    # Buttons layout
    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ("C", 5, 0), ("√", 5, 1), ("%", 5, 2)
    ]

    for (text, row, col) in buttons:
        action = None
        if text == "=":
            action = calc.calculate
        elif text == "C":
            action = calc.reset
        elif text == "√":
            action = calc.sqrt
        elif text == "%":
            action = calc.percent
        else:
            action = lambda t=text: calc.insert(t)

        color = operator_color if text in ["/", "*", "-", "+", "=", "%", "√"] else button_color

        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 16),
            height=2,
            width=5,
            command=action,
            bg=color,
            fg=text_color,
            activebackground=button_active,
            activeforeground=text_color,
            relief="flat",
            bd=0
        )
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # Make buttons responsive
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)

    # Keyboard input binding
    def on_key(event):
        if event.keysym == "Return":
            calc.calculate()
        elif event.keysym == "Escape":
            calc.reset()
        else:
            entry.insert(tk.END, event.char)

    root.bind("<Key>", on_key)

    root.mainloop()

if __name__ == "__main__":
    main()
