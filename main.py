from pathlib import Path
from filters import rotation
from filters import flip 

path = 'images/'

dirpath = Path(path)

for file in dirpath.iterdir():
    rotation.rotation(file, path)
    flip.flip(file, path)