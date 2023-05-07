#Generating Random Numbers and Guessing those numbers by user input

"""
Requirements to win the game faster :
1. Luck
2. Simple Calculations
"""

import random
import tkinter as tk
from tkinter import messagebox

def key(r):
    for widget in root.winfo_children(): widget.destroy()
    count=0
    def check():
        nonlocal count
        x = int(guess_number.get())
        count +=1
        if x == r:
            messagebox.showinfo("Congratulations",f"You guessed it !!!\n Number of tirals taken:{count}")
            reset_game()
        elif x > r:
            y = str(x)
            messagebox.showinfo("Incorrect", "Number is lesser than " + y)
        else:
            y = str(x)
            messagebox.showinfo("Incorrect", "Number is greater than " + y)
    
    label = tk.Label(root, text="Guess a number between 0 and 100:", font=("Helvetica", 18), fg="white", bg="#333333")
    label.pack(pady=20)
    guess_number = tk.Entry(root, font=("Helvetica", 20))
    guess_number.pack(pady=12)
    check_button = tk.Button(root, text="Check", command=check, font=("Helvetica", 12), fg="white", bg="#555555")
    check_button.pack(pady=12)

def new():
    for widget in root.winfo_children(): widget.destroy()   
    label = tk.Label(root, text="Wanna Guess ?", font=("Helvetica", 30), fg="white", bg="#333333")
    label.pack(pady=30)
    yes_button = tk.Button(root, text="Yes", command=yes, font=("Helvetica", 15), fg="white", bg="#555555")
    yes_button.place(x=100, y=120)
    no_button = tk.Button(root, text="No", command=no, font=("Helvetica", 15), fg="white", bg="#555555")
    no_button.place(x=240, y=120)

def reset_game():
    for widget in root.winfo_children(): widget.destroy()
    new()

def new_rand():
    for widget in root.winfo_children(): widget.destroy()
    
    def rand():
        for widget in root.winfo_children(): widget.destroy()
        z = random.randint(0, 100) 
        #print(z)   #Print the Random Number that is Generated
        key(z)
        
    def assign():
        for widget in root.winfo_children(): widget.destroy()
        def number():
            x = int(guess_number.get())
            key(x)
        label = tk.Label(root, text="Enter a number :", font=("Helvetica", 16), fg="white", bg="#333333")
        label.pack(pady=20)
        guess_number = tk.Entry(root, font=("Helvetica", 20))
        guess_number.pack(pady=10)
        check_button = tk.Button(root, text="Assign", command=number, font=("Helvetica", 12), fg="white", bg="#555555")
        check_button.pack(pady=10)
    
    label = tk.Label(root, text="Choose Mode ?", font=("Helvetica", 25), fg="white", bg="#333333")
    label.pack(pady=30)
    yes_button = tk.Button(root, text="Random Number", command=rand, font=("Helvetica", 12), fg="white", bg="#555555")
    yes_button.place(x=210, y=120)
    no_button = tk.Button(root, text="Assign a Number", command=assign, font=("Helvetica", 12), fg="white", bg="#555555")
    no_button.place(x=40, y=120)

def no():root.destroy()

def yes():
    for widget in root.winfo_children(): widget.destroy()
    new_rand()
    

root = tk.Tk()
root.title("Keep Guessing")
root.geometry("400x200")
root.configure(bg="#333333")

label = tk.Label(root, text="Wanna Guess ?", font=("Helvetica", 30), fg="white", bg="#333333")
label.pack(pady=30)
yes_button = tk.Button(root, text="Yes", command=yes, font=("Helvetica", 15), fg="white", bg="#555555")
yes_button.place(x=100, y=120)
no_button = tk.Button(root, text="No", command=no, font=("Helvetica", 15), fg="white", bg="#555555")
no_button.place(x=240, y=120)

root.mainloop()