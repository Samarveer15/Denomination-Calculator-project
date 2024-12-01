import tkinter as tk
from tkinter import ttk

def check_password_strength():
    password = entry.get()
    length = len(password)
    
    if length <= 5:
        strength = "Weak"
        color = "Red"
    elif length <= 8:
        strength = "Medium"
        color = "Yellow"
    elif length <= 12:
        strength = "Strong"
        color = "Light Green"
    else:
        strength = "Very Strong"
        color = "Dark Green"
    
    result_label.config(text=f"Strength: {strength}", foreground=color)

root = tk.Tk()
root.geometry("400x400")
root.title("Password Strength Checker")

ttk.Label(root, text="Enter your password:").pack(pady=10)
entry = ttk.Entry(root, show="*")
entry.pack(pady=10)

check_button = ttk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
