import tkinter as tk

def open_login(root, open_dashboard):
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("400x300")

    tk.Label(login_window, text="Login", font=("Arial", 18)).pack(pady=10)

    # Username
    tk.Label(login_window, text="Username").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    # Password
    tk.Label(login_window, text="Password").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    def handle_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        print(f"Username: '{username}'")
        print(f"Password: '{password}'")

        # later: connect Soham's DB here
        if username.strip() == "admin" and password.strip() == "1234":
            print("Login successful")
            login_window.destroy()
            open_dashboard(username)
        else:
            print("Invalid credentials")

    tk.Button(login_window, text="Login", command=handle_login).pack(pady=10)