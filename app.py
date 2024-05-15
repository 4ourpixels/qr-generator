from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()


def generate():
    global file_name
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    display_qr_code(file_name)


def display_qr_code(file_name):
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)


def download_qr_code():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        import shutil
        shutil.copyfile(file_name, file_path)


canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator",
                  fg='blue', font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link Name")
link_label = Label(root, text="Link")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

button_generate = Button(text="Generate QR Code", command=generate)
canvas.create_window(200, 230, window=button_generate)

button_download = Button(text="Download QR Code", command=download_qr_code)
canvas.create_window(200, 260, window=button_download)

root.mainloop()
