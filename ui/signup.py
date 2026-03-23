import tkinter as tk
from tkinter import messagebox
from database.auth import signup

selected_avatar = None

def open_signup(root):

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#020617")

    tk.Label(root, text="Sign Up", font=("Arial", 30), fg="white", bg="#020617").pack(pady=20)

    username_entry = tk.Entry(root, font=("Arial", 14))
    username_entry.pack(pady=10)

    password_entry = tk.Entry(root, font=("Arial", 14), show="*")
    password_entry.pack(pady=10)

    tk.Label(root, text="Choose Avatar", fg="white", bg="#020617").pack(pady=10)

    avatars = ["daya", "abhijeet", "pradyuman", "tarika"]

    def select_avatar(a):
        global selected_avatar
        selected_avatar = a
        messagebox.showinfo("Avatar", f"Selected {a}")

    for a in avatars:
        tk.Button(root, text=a, command=lambda x=a: select_avatar(x)).pack()

    def handle_signup():
        username = username_entry.get()
        password = password_entry.get()

        if not selected_avatar:
            messagebox.showerror("Error", "Select Avatar")
            return

        if signup(username, password, selected_avatar):
            messagebox.showinfo("Success", "Account Created")
        else:
            messagebox.showerror("Error", "User already exists")

    tk.Button(root, text="Create Account", command=handle_signup).pack(pady=20)