import tkinter as tk
from PIL import Image, ImageTk
from Database.db import connect_db
from ui.game import start_game

selected_avatar = None

def open_avatar_select(root, username):

    global selected_avatar
    selected_avatar = None

    avatar_window = tk.Toplevel(root)
    avatar_window.title("CIS // Select Avatar")
    avatar_window.geometry("700x500")
    avatar_window.configure(bg="black")

    # Center window
    x = (avatar_window.winfo_screenwidth() // 2) - 350
    y = (avatar_window.winfo_screenheight() // 2) - 250
    avatar_window.geometry(f"700x500+{x}+{y}")

    # ===== TITLE =====
    tk.Label(
        avatar_window,
        text="SELECT YOUR AVATAR",
        font=("Consolas", 22, "bold"),
        fg="#00f5ff",
        bg="black"
    ).pack(pady=20)

    tk.Label(
        avatar_window,
        text="> Choose your investigator identity",
        font=("Consolas", 11),
        fg="#00ff9f",
        bg="black"
    ).pack()

    # ===== FRAME =====
    frame = tk.Frame(avatar_window, bg="black")
    frame.pack(pady=30)

    avatars = [
        ("daya", "assets/avatars/daya.png"),
        ("siddhesh", "assets/avatars/siddhesh.png"),
        ("pradyuman", "assets/avatars/pradyuman.png"),
        ("tarika", "assets/avatars/tarika.png")
    ]

    avatar_widgets = []

    def select_avatar(name, widget):
        global selected_avatar
        selected_avatar = name

        # Remove highlight from all
        for w in avatar_widgets:
            w.config(highlightthickness=0)

        # Highlight selected
        widget.config(highlightbackground="#00ff9f", highlightthickness=3)

    # ===== LOAD AVATARS =====
    for i, (name, path) in enumerate(avatars):

        img = Image.open(path)
        img = img.resize((120, 120))
        photo = ImageTk.PhotoImage(img)

        card = tk.Label(
            frame,
            image=photo,
            bg="#020617",
            cursor="hand2"
        )
        card.image = photo
        card.grid(row=0, column=i, padx=15)

        card.bind("<Button-1>", lambda e, n=name, w=card: select_avatar(n, w))

        # Hover effect
        def on_enter(e):
            e.widget.config(bg="#00ff9f")

        def on_leave(e):
            e.widget.config(bg="#020617")

        card.bind("<Enter>", on_enter)
        card.bind("<Leave>", on_leave)

        # Name
        tk.Label(
            frame,
            text=name.upper(),
            font=("Consolas", 10),
            fg="#00ff9f",
            bg="black"
        ).grid(row=1, column=i, pady=5)

        avatar_widgets.append(card)

    # ===== CONFIRM BUTTON =====
    def confirm():

        if not selected_avatar:
            return

        # Save to DB
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET avatar=? WHERE username=?",
            (selected_avatar, username)
        )

        conn.commit()
        conn.close()

        avatar_window.destroy()
        start_game()   # 🔥 SAME AS YOUR GAME FLOW

    tk.Button(
        avatar_window,
        text="CONFIRM AGENT",
        font=("Consolas", 12, "bold"),
        bg="#020617",
        fg="#00ff9f",
        activebackground="#00f5ff",
        activeforeground="black",
        width=25,
        pady=5,
        command=confirm
    ).pack(pady=20)