import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Encoder Decoder Tool")
root.geometry("900x600")
root.resizable(False, False)

# ---------------- BACKGROUND IMAGE ----------------
bg_path = os.path.join("asset", "background.jpg")

try:
    bg_img = Image.open(bg_path)
    bg_img = bg_img.resize((900, 600))
    bg_photo = ImageTk.PhotoImage(bg_img)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0)
except Exception as e:
    print("Background not loaded:", e)

# ---------------- ENCODE WINDOW ----------------
def encode_window():
    win = tk.Toplevel(root)
    win.title("Encode Message")
    win.geometry("400x300")
    win.resizable(False, False)

    tk.Label(win, text="Message").pack(pady=5)
    msg = tk.Entry(win, width=30)
    msg.pack(pady=5)

    tk.Label(win, text="Key").pack(pady=5)
    key = tk.Entry(win, width=30)
    key.pack(pady=5)

    result = tk.Label(win, text="")
    result.pack(pady=10)

    def encode():
        try:
            text = msg.get()
            k = int(key.get())
            encoded = ''.join(chr(ord(c) + k) for c in text)
            result.config(text=f"Encoded: {encoded}")
        except:
            messagebox.showerror("Error", "Key must be a number")

    tk.Button(win, text="Encode", command=encode).pack(pady=10)

# ---------------- DECODE WINDOW ----------------
def decode_window():
    win = tk.Toplevel(root)
    win.title("Decode Message")
    win.geometry("400x300")
    win.resizable(False, False)

    tk.Label(win, text="Message").pack(pady=5)
    msg = tk.Entry(win, width=30)
    msg.pack(pady=5)

    tk.Label(win, text="Key").pack(pady=5)
    key = tk.Entry(win, width=30)
    key.pack(pady=5)

    result = tk.Label(win, text="")
    result.pack(pady=10)

    def decode():
        try:
            text = msg.get()
            k = int(key.get())
            decoded = ''.join(chr(ord(c) - k) for c in text)
            result.config(text=f"Decoded: {decoded}")
        except:
            messagebox.showerror("Error", "Key must be a number")

    tk.Button(win, text="Decode", command=decode).pack(pady=10)

# ---------------- MAIN BUTTONS ----------------
tk.Label(
    root,
    text="Encode Decode Tool",
    font=("Arial", 18, "bold"),
    bg="white"
).pack(pady=40)

tk.Button(root, text="Encode", width=20, command=encode_window).pack(pady=10)
tk.Button(root, text="Decode", width=20, command=decode_window).pack(pady=10)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=10)

root.mainloop()