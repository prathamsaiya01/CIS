import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def show_splash(root, next_screen_callback):
    splash = tk.Toplevel(root)
    splash.title("CIS - Loading")
    splash.geometry("600x400")
    splash.configure(bg="black")

    # Center window
    x = (splash.winfo_screenwidth() // 2) - (600 // 2)
    y = (splash.winfo_screenheight() // 2) - (400 // 2)
    splash.geometry(f"600x400+{x}+{y}")

    # Remove title bar
    splash.overrideredirect(True)

    # Load Logo
    logo_path = os.path.join("assets", "logo.png")
    img = Image.open(logo_path)
    img = img.resize((200, 200))
    logo = ImageTk.PhotoImage(img)

    logo_label = tk.Label(splash, image=logo, bg="black")
    logo_label.image = logo
    logo_label.pack(pady=20)

    # Title
    title = tk.Label(
        splash,
        text="CIS",
        font=("Arial", 28, "bold"),
        fg="white",
        bg="black"
    )
    title.pack()

    subtitle = tk.Label(
        splash,
        text="Crime Investigation System",
        font=("Arial", 14),
        fg="gray",
        bg="black"
    )
    subtitle.pack(pady=5)

    # Progress Bar
    progress = ttk.Progressbar(splash, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=30)

    def load():
        for i in range(101):
            progress['value'] = i
            splash.update_idletasks()
            splash.after(20)

        splash.destroy()
        next_screen_callback()

    splash.after(500, load)