import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = Image.open(BytesIO(response.content))
        image_data.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image_data)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None

def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)

    if img is not None:
        new_window = tk.Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry("600x480")
        label = tk.Label(new_window, image=img)
        label.pack()
        label.image = img

window = tk.Tk()
window.title("Cats")
window.geometry("600x480")

tag_entry = tk.Entry()
tag_entry.pack()

load_button = tk.Button(window, text="Загрузить по тэгу", command=open_new_window)
load_button.pack()

menubar = tk.Menu(window)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить кота", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.quit)

url = 'https://cataas.com/cat'

window.mainloop()