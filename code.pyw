import sys
import os 

from PIL import Image
filePath = sys.argv[1]

for value in sys.argv[2:]:

    filePath = filePath + " "  + value

image = Image.open(filePath)

name = os.path.splitext(os.path.basename(filePath))[0]

image = image.convert("RGB")
image.save(name + "-updated" + ".jpg")

os.remove(filePath)
