from PIL import Image, ImageFilter
from datetime import datetime

def edger(file, path):
    with Image.open(file) as im:
        name = str(datetime.now())+ ".jpg"
        image = im.convert('L')
        image = image.filter(ImageFilter.FIND_EDGES)
        image.save(path + name)
