import os
from pathlib import Path
from PIL import Image

path = 'images'

dirpath = Path(path)

for files in dirpath.iterdir():
    with Image.open(files) as im:
        results = im.rotate(35)
        results.show()
