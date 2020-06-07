from tkinter import messagebox

def show_error(message):
    messagebox.showerror('Error', message)
    
def show_message(message):
    messagebox.showinfo('Success', message)