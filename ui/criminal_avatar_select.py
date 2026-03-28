import tkinter as tk
from PIL import Image, ImageTk
from Database.db import connect_db
from ui.criminal_game import start_criminal_game

selected_avatar = None

def open_criminal_avatar_select(root, username):

    global selected_avatar
    selected_avatar = None

    window = tk.Toplevel(root)
    window.title("CIS // Select Criminal Identity")
    window.geometry("750x520")
    window.configure(bg="black")

    # Center
    x = (window.winfo_screenwidth() // 2) - 375
    y = (window.winfo_screenheight() // 2) - 260
    window.geometry(f"750x520+{x}+{y}")

    # ===== TITLE =====
    tk.Label(
        window,
        text="SELECT YOUR IDENTITY",
        font=("Consolas", 22, "bold"),
        fg="#ff004f",
        bg="black"
    ).pack(pady=20)

    tk.Label(
        window,
        text="> Choose your criminal alias",
        font=("Consolas", 11),
        fg="#ff4d4d",
        bg="black"
    ).pack()

    # ===== FRAME =====
    frame = tk.Frame(window, bg="black")
    frame.pack(pady=30)

    avatars = [
        ("shadow", "assets/avatars_criminal/shadow.png"),
        ("viper", "assets/avatars_criminal/viper.png"),
        ("ghost", "assets/avatars_criminal/ghost.png"),
        ("cipher", "assets/avatars_criminal/cipher.png")
    ]

    widgets = []

    def select_avatar(name, widget):
        global selected_avatar
        selected_avatar = name

        for w in widgets:
            w.config(highlightthickness=0)

        widget.config(highlightbackground="#ff004f", highlightthickness=3)

    # ===== LOAD IMAGES =====
    for i, (name, path) in enumerate(avatars):

        img = Image.open(path)
        img = img.resize((130, 130))
        photo = ImageTk.PhotoImage(img)

        lbl = tk.Label(
            frame,
            image=photo,
            bg="#020617",
            cursor="hand2"
        )
        lbl.image = photo
        lbl.grid(row=0, column=i, padx=15)

        lbl.bind("<Button-1>", lambda e, n=name, w=lbl: select_avatar(n, w))

        # Hover effect
        def on_enter(e):
            e.widget.config(bg="#ff004f")

        def on_leave(e):
            e.widget.config(bg="#020617")

        lbl.bind("<Enter>", on_enter)
        lbl.bind("<Leave>", on_leave)

        tk.Label(
            frame,
            text=name.upper(),
            font=("Consolas", 10),
            fg="#ff4d4d",
            bg="black"
        ).grid(row=1, column=i, pady=5)

        widgets.append(lbl)

    # ===== CONFIRM =====
    def confirm():

        if not selected_avatar:
            return

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET avatar=? WHERE username=?",
            (selected_avatar, username)
        )

        conn.commit()
        conn.close()

        window.destroy()
        start_criminal_game()

    tk.Button(
        window,
        text="CONFIRM IDENTITY",
        font=("Consolas", 12, "bold"),
        bg="#020617",
        fg="#ff004f",
        activebackground="#ff004f",
        activeforeground="black",
        width=25,
        pady=5,
        command=confirm
    ).pack(pady=20)