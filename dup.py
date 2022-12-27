from PIL import Image
from os import listdir
from os.path import isfile, join

p = "/Users/zciw/Pictures/Biblioteka Zdjęć.photoslibrary/originals/0/066CEE5D-C874-4D16-A6B7-A3BB13EDE3EF.jpeg"

path = "/Users/zciw/Pictures/Biblioteka Zdjęć.photoslibrary/originals/0/"

fl = [f for f in listdir(path) if isfile(join(path, f))]

l = []



def showColor(filePath):
    with Image.open(filePath) as img:
        pix = img.load()
        print(f"img size {img.size}")
        l.Append(img.size)
        print(pix[1,1])

for i in fl:
    p = path + i
    if p[-1] == "g":
        showColor(p)

