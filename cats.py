import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = Image.open(BytesIO(response.content))
        return ImageTk.PhotoImage(image_data)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None

def set_image():
    img = load_image(url)
    if img is not None:
        label.configure(image=img)
        label.image = img

window = tk.Tk()
window.title("Cats")
window.geometry("600x480")

label = tk.Label()
label.pack()

update_button = tk.Button(window, text="Ещё котика!", command=set_image)
update_button.pack()

url = 'https://cataas.com/cat'
set_image()

window.mainloop()