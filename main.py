import tkinter as tk
from ui.splash import show_splash

def open_login():
    print("Go to Login Screen")  # we’ll replace later

root = tk.Tk()
root.withdraw()  # hide main window

show_splash(root, open_login)

root.mainloop()