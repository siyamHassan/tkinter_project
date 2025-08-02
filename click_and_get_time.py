import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("400x400")
root.config(bg="green")
def show():
    import datetime
    time = datetime.datetime.now()
    time = time.strftime("%X")
    messagebox.showinfo("time is",f"time is {time}")
    print('hello world')
text_lable = tk.Label(text="if you click below this button \n you can see the current time")
text_lable.pack(pady=10)
tk.Button(root,text='show',command=show).pack(pady=10)
root.mainloop()