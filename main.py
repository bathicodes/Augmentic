from pathlib import Path
from filters import rotation as rt

path = 'images/'

dirpath = Path(path)

for file in dirpath.iterdir():
    rt.rotation(file, path)