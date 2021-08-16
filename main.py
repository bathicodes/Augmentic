from pathlib import Path
from PIL import Image
from datetime import datetime

path = '/Users/bathiyaseneviratne/Desktop/images/'

dirpath = Path(path)

for files in dirpath.iterdir():
    with Image.open(files) as im:
        name = str(datetime.now())+ ".jpg"
        image = im.rotate(35)
        image.save(path + name)
