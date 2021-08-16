from PIL import Image
from datetime import datetime


def rotation(file, path):
    with Image.open(file) as im:
        name = str(datetime.now())+ ".jpg"
        image = im.rotate(35)
        image.save(path + name)