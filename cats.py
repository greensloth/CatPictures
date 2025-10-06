import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image

window = tk.Tk()
window.title("Cats")
window.geometry("600x480")

label = tk.Label()
label.pack()

url = 'https://cataas.com/cat'
img = load_image(url)

if img is not None:
    label.configure(image=img)
    label.image = img

window.mainloop()