from pathlib import Path
from filters import rotation
from filters import flip 
from filters import grayscales
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog

def augmentation():
    try:
        # variable
        file_counter = 0
        reject_counter = 0
        affect_counter = 0

        # select path
        path = filedialog.askdirectory()
        save_path = path + '/'

        dirpath = Path(path)

        for file in dirpath.iterdir():
            file_counter += 1
            if file.suffix.lower() in [".png",".jpg",".jpeg",".tif", ".tiff",".bmp",".gif",".eps"]:
                rotation.rotation(file, save_path)
                flip.flip(file, save_path)
            else:
                reject_counter += 1
                pass

        for file in dirpath.iterdir():
            affect_counter += 1

        lbl3.config(text=f"Selected Files : {file_counter}")
        lbl5.config(text=f"Rejected Files : {reject_counter}", fg="red")
        lbl6.config(text=f"Generated Files : {affect_counter - (reject_counter + file_counter)}", fg="green")

    except:
        tkinter.messagebox.showerror("Oops!", "No file has been selected")


def grayscale():
    try:
        # variable
        file_counter = 0
        reject_counter = 0
        affect_counter = 0

        # select path
        path = filedialog.askdirectory()
        save_path = path + '/'

        dirpath = Path(path)

        for file in dirpath.iterdir():
            file_counter += 1
            if file.suffix.lower() in [".png",".jpg",".jpeg",".tif", ".tiff",".bmp",".gif",".eps"]:
                grayscales.grayscaler(file, save_path)
            else:
                reject_counter += 1
                pass

        for file in dirpath.iterdir():
            affect_counter += 1

        lbl3.config(text=f"Selected Files : {file_counter}")
        lbl5.config(text=f"Rejected Files : {reject_counter}", fg="red")
        lbl6.config(text=f"Generated Files : {affect_counter - (reject_counter + file_counter)}", fg="green")

    except:
        tkinter.messagebox.showerror("Oops!", "No file has been selected")


# ************************************************************

root = Tk()
root.title("Augmentic")
root.resizable(False, False)

window_height = 400
window_width = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

lbl1 = Label(root, text="Augmentic",fg="#7c40ff")
lbl1.config(font=("Helvetica bold", 20))
lbl1.pack(pady=10)

lbl3 = Label(root, text="Selected Files : 0")
lbl3.config(font=("Arial", 15))
lbl3.pack(pady=3)

lbl5 = Label(root, text="Rejected Files : 0", fg="red")
lbl5.config(font=("Arial", 15))
lbl5.pack(pady=3)

lbl6 = Label(root, text="Generated Files : 0", fg="green")
lbl6.config(font=("Arial", 15))
lbl6.pack(pady=3)

lbl2 = Label(root, text="Developed by Bathiya Seneviratne", fg="red", font=("Arial", 12), bg="#f1f1f1")
lbl2.pack(side=BOTTOM, fill=X)

button = Button(root, text="Augmentation", width=20, height=2, command=augmentation)
button.pack(side=BOTTOM, pady=10)

button1 = Button(root, text="Grayscale", width=20, height=2, command=grayscale)
button1.pack(side=BOTTOM, pady=10)

root.mainloop()