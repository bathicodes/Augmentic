from PIL import Image
from datetime import datetime

def flip(file, path):
    with Image.open(file) as im:
        name = str(datetime.now())+ ".jpg"
        image = im.transpose(Image.FLIP_LEFT_RIGHT)
        image.save(path + name)
