from PIL import Image
from datetime import datetime

def grayscaler(file, path):
    with Image.open(file) as im:
        name = str(datetime.now())+ ".jpg"
        image = im.convert('L')
        image.save(path + name)
