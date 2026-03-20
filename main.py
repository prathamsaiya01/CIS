import tkinter as tk
from ui.splash import show_splash
from ui.login import open_login
from ui.dashboard import open_dashboard

root = tk.Tk()
root.withdraw()  # hide main window

show_splash(root, lambda: open_login(root, open_dashboard))

root.mainloop()

