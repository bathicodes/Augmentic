from PIL import Image
from datetime import datetime

rotation_angles = [10,20,30,40,50,60,70,80,90,100]

## Uncomment this part if you want black background 

# def rotation(file, path):
#     for angles in rotation_angles:
#         with Image.open(file) as im:
#             name = str(datetime.now())+ ".jpg"
#             image = im.rotate(angles)
#             image.save(path + name)

 ##  this part provides you want white background 
           
def rotation(file, path):
    for angles in rotation_angles:
        with Image.open(file) as im:
            name = str(datetime.now())+ ".jpg"
            im2 = im.convert('RGBA')
            rot = im2.rotate(angles, expand=1)
            fff = Image.new('RGBA', rot.size, (255,)*4)
            out = Image.composite(rot, fff, rot)
            out.convert(im.mode).save(path + name)