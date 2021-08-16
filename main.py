from pathlib import Path
from filters import rotation
from filters import flip 
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog

def main_loop():

    # select path
    path = filedialog.askdirectory()
    save_path = path + '/'

    dirpath = Path(path)

    for file in dirpath.iterdir():
        if file.suffix in [".png",".jpg",".jpeg",".tif", ".tiff",".bmp",".gif",".eps"]:
            rotation.rotation(file, save_path)
            flip.flip(file, save_path)
        else:
            pass


# ************************************************************

root = Tk()
root.title("Augmentic")
root.resizable(False, False)

window_height = 280
window_width = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

lbl1 = Label(root, text="Augmentic",fg="#7c40ff")
lbl1.config(font=("Helvetica bold", 20))
lbl1.pack(pady=10)

lbl3 = Label(root, text="Image status : Pending")
lbl3.config(font=("Arial", 15))
lbl3.pack(pady=10)

lbl2 = Label(root, text="Developed by Bathiya Seneviratne", fg="red", font=("Arial", 12), bg="#f1f1f1")
lbl2.pack(side=BOTTOM, fill=X)

lbl4 = Label(root, text="GitHub (@bathicodes)", fg="red", font=("Arial", 12), bg="#f1f1f1")
lbl4.pack(side=BOTTOM, fill=X)

but = Button(root, text="Select & Save", width=20, height=2, command=main_loop)
but.pack(side=BOTTOM, pady=10)

root.mainloop()