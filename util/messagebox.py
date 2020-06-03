from tkinter import messagebox

class MessageDialog:
    
    def show_message(self, message):
        messagebox.showinfo('', message)
    
    def ask_message(self, message):
        return messagebox.askyesno('', message)