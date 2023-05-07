#Generating Random Numbers and Guessing those numbers by user input

"""
Requirements to win the game faster :
1. Luck
2. Simple Calculations
"""

import random   #Random variable generator
import tkinter as tk    #Tkinter provides classes which allow the display, positioning and control of widgets
from tkinter import messagebox  #messagebox is a module from tkinter

# Function to check the user's guess
def key(r):
    for widget in root.winfo_children(): widget.destroy()   #winfo_children() - Returns a list of all widgets which are children of this widget
    count=0
    def check():
        nonlocal count
        x = int(guess_number.get())   # Get the user's guess from the input field
        count +=1   # Increment the trial count
        
        # Compare the user's guess with the target number and provide feedback
        if x == r:
            messagebox.showinfo("Congratulations",f"You guessed it !!!\n Number of Trials taken :{count}")
            reset_game()    #
        elif x > r:
            y = str(x)
            messagebox.showinfo("Incorrect", "Number is lesser than " + y)
        else:
            y = str(x)
            messagebox.showinfo("Incorrect", "Number is greater than " + y)
     # Create a label for the guessing prompt
    label = tk.Label(root, text="Guess a number between 0 and 100:", font=("Helvetica", 18), fg="white", bg="#333333")
    label.pack(pady=20)
    
    # Create an entry field for the user's guess
    guess_number = tk.Entry(root, font=("Helvetica", 20))
    guess_number.pack(pady=12)
    
    # Create a button to check the user's guess
    check_button = tk.Button(root, text="Check", command=check, font=("Helvetica", 12), fg="white", bg="#555555")
    check_button.pack(pady=12)


# Function to start a new game
def new():
    for widget in root.winfo_children():    # Destroy all previous UI elements
        widget.destroy()
        
    # Create a label asking if the user wants to guess
    label = tk.Label(root, text="Wanna Guess ?", font=("Helvetica", 30), fg="white", bg="#333333")
    label.pack(pady=30)
    
    # Create buttons for "Yes" and "No"
    yes_button = tk.Button(root, text="Yes", command=mode, font=("Helvetica", 15), fg="white", bg="#555555")
    yes_button.place(x=100, y=120)
    
    no_button = tk.Button(root, text="No", command=no, font=("Helvetica", 15), fg="white", bg="#555555")
    no_button.place(x=240, y=120)

# Function to reset the game
def reset_game():
    for widget in root.winfo_children():    # Destroy all previous UI elements 
        widget.destroy()
    new()   # Function to start a new game

# Function to choose the game mode
def mode():
    for widget in root.winfo_children():    # Destroy all previous UI elements 
        widget.destroy()
        
    #random Mode
    def rand():
        for widget in root.winfo_children():
            widget.destroy()
        z = random.randint(0, 100)  #Return random integer in range [a, b], including both end points.
        #print(z)   #Print the Random Number that is Generated
        key(z)
    
    def assign():
        for widget in root.winfo_children():
            widget.destroy()
        
        # Function to assign a target number manually
        def number():
            x = int(guess_number.get())
            key(x)
        
        # Create a label asking the user to enter a number
        label = tk.Label(root, text="Enter a number :", font=("Helvetica", 16), fg="white", bg="#333333")
        label.pack(pady=20)
        
        # Create an entry field for the user to enter a number
        guess_number = tk.Entry(root, font=("Helvetica", 20))
        guess_number.pack(pady=10)
        
        # Create a button to assign the number and start the game
        check_button = tk.Button(root, text="Assign", command=number, font=("Helvetica", 12), fg="white", bg="#555555")
        check_button.pack(pady=10)
    
    # Create a label asking the user to choose the game mode
    label = tk.Label(root, text="Choose Mode ?", font=("Helvetica", 25), fg="white", bg="#333333")
    label.pack(pady=30)
    
    # Create buttons for "Random Number" and "Assign a Number"
    yes_button = tk.Button(root, text="Random Number", command=rand, font=("Helvetica", 12), fg="white", bg="#555555")
    yes_button.place(x=210, y=120)
    no_button = tk.Button(root, text="Assign a Number", command=assign, font=("Helvetica", 12), fg="white", bg="#555555")
    no_button.place(x=40, y=120)

# Destroy the main window, terminating the program
def no():
    root.destroy()    # Destroy the main window, terminating the program    
    
root = tk.Tk()     # Create a main window using tkinter
root.title("Keep Guessing")    # Set the title of the window to "Keep Guessing"
root.geometry("400x200")    # Set the size of the window to 400x200 pixels 
root.configure(bg="#333333")    # Set the background color of the window to a dark gray

# Create a label asking if the user wants to guess
label = tk.Label(root, text="Wanna Guess ?", font=("Helvetica", 30), fg="white", bg="#333333")
label.pack(pady=30)

# Create buttons for "Yes" and "No"
yes_button = tk.Button(root, text="Yes", command=mode, font=("Helvetica", 15), fg="white", bg="#555555")
yes_button.place(x=100, y=120)

no_button = tk.Button(root, text="No", command=no, font=("Helvetica", 15), fg="white", bg="#555555")
no_button.place(x=240, y=120)

root.mainloop()     # Run the main event loop of the tkinter application
