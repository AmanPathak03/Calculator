import tkinter as tk
from tkinter import messagebox
import math

class AdvancedCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")
        master.geometry("400x600")
        
        # User Age Group Selection
        self.age_label = tk.Label(master, text="Select Age Group", font=("Arial", 12))
        self.age_label.pack(pady=10)
        
        self.age_var = tk.StringVar(value="")
        self.age_10_20 = tk.Radiobutton(master, text="10-20 Years", 
                                        variable=self.age_var, 
                                        value="10-20", 
                                        command=self.set_calculator_mode)
        self.age_10_20.pack()
        
        self.age_over_20 = tk.Radiobutton(master, text="Over 20 Years", 
                                          variable=self.age_var, 
                                          value="over-20", 
                                          command=self.set_calculator_mode)
        self.age_over_20.pack()
        
        # Calculator Frame
        self.calc_frame = tk.Frame(master)
        self.calc_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Display
        self.display = tk.Entry(self.calc_frame, width=30, justify='right', font=("Arial", 14))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Buttons
        self.create_buttons()
        
        # Mode tracking
        self.current_mode = None
        
    def set_calculator_mode(self):
        # Clear previous buttons
        for widget in self.calc_frame.winfo_children()[1:]:
            widget.destroy()
        
        # Set mode based on age group
        if self.age_var.get() == "10-20":
            self.create_basic_buttons()
            self.current_mode = "basic"
            messagebox.showinfo("Mode", "Basic Calculator Mode for 10-20 Years")
        elif self.age_var.get() == "over-20":
            self.create_advanced_buttons()
            self.current_mode = "advanced"
            messagebox.showinfo("Mode", "Scientific Calculator Mode for Over 20 Years")
        else:
            messagebox.showwarning("Warning", "Please select an age group")
    
    def create_basic_buttons(self):
        # Basic buttons for 10-20 age group
        basic_buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row, col = 1, 0
        for button in basic_buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.calc_frame, text=button, width=10, height=2, command=cmd).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear button
        tk.Button(self.calc_frame, text='C', width=10, height=2, command=self.clear).grid(row=row, column=col, padx=2, pady=2)
    
    def create_advanced_buttons(self):
        # Advanced buttons for over 20 age group
        advanced_buttons = [
            '7', '8', '9', '/', 'sin', 
            '4', '5', '6', '*', 'cos', 
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'log',
            '(', ')', '^', 'sqrt', 'exp'
        ]
        
        row, col = 1, 0
        for button in advanced_buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.calc_frame, text=button, width=8, height=2, command=cmd).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 4:
                col = 0
                row += 1
        
        # Clear button
        tk.Button(self.calc_frame, text='C', width=8, height=2, command=self.clear).grid(row=row, column=col, padx=2, pady=2)
    
    def create_buttons(self):
        # Placeholder method to prevent errors before mode selection
        pass
    
    def click(self, key):
        if key == '=':
            try:
                # Handle special scientific functions
                if self.current_mode == 'advanced':
                    # Replace special function names with math library equivalents
                    result = self.display.get().replace('^', '**')
                    result = result.replace('sin(', 'math.sin(')
                    result = result.replace('cos(', 'math.cos(')
                    result = result.replace('tan(', 'math.tan(')
                    result = result.replace('log(', 'math.log(')
                    result = result.replace('sqrt(', 'math.sqrt(')
                    result = result.replace('exp(', 'math.exp(')
                    
                    # Evaluate the expression
                    result = eval(result)
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                else:
                    # Basic mode calculation
                    result = eval(self.display.get())
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif key == 'C':
            self.clear()
        else:
            self.display.insert(tk.END, key)
    
    def clear(self):
        self.display.delete(0, tk.END)

def main():
    root = tk.Tk()
    calculator = AdvancedCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()