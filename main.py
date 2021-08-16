from pathlib import Path
from filters import rotation as rotation

path = 'images/'

dirpath = Path(path)

for file in dirpath.iterdir():
    rotation.rotation(file, path)