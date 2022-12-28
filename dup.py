from PIL import Image
from os import listdir
from os.path import isfile, join

path = "/Users/zciw/Pictures/Biblioteka Zdjęć.photoslibrary/originals/1/"

fl = [f for f in listdir(path) if isfile(join(path, f))]

l = []
suspectedDuplicateCounter = 0

def showColor(filePath):
    with Image.open(filePath) as img:
        pix = img.load()
        obj = [img.size, pix[1,1], pix[img.size[0]/2, 2]]
        if obj not in l:
            l.append(l)

        else:
            print(obj)
            print(filePath)
            suspectedDuplicateCounter+=1

for i in fl:
    p = path + i
    if p[-1] == "g" and p[-3] != "m":
        showColor(p)
        print(p)
print(f"liczba unikatowych zdjęć: {len(l)}, liczba podejżanych duplikatów {suspectedDuplicateCounter} ")
