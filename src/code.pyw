import sys
import os 

from PIL import Image
filePath = sys.argv[1]

for value in sys.argv[2:]:

    filePath = filePath + " "  + value

image = Image.open(filePath)

image.save(os.path.dirname(filePath) + "\\" + name + "-updated" + ".jpg")

image = image.convert("RGB")
image.save(name + "-updated" + ".jpg")

os.remove(filePath)
