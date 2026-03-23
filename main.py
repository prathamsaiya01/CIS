import tkinter as tk
from ui.splash import show_splash
from ui.login import open_login
from Database.db import create_tables

root = tk.Tk()
root.withdraw()

create_tables()   # 🔥 important

show_splash(root, lambda: open_login(root))

root.mainloop()