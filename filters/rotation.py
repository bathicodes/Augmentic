from PIL import Image
from datetime import datetime

rotation_angles = [10,20,30,40,50,60,70,80,90,100]

def rotation(file, path):
    for angles in rotation_angles:
        with Image.open(file) as im:
            name = str(datetime.now())+ ".jpg"
            image = im.rotate(angles)
            image.save(path + name)