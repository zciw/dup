import os
from PIL import Image
from os import listdir
from os.path import isfile, join

path = "/Users/zciw/Pictures/Biblioteka Zdjęć.photoslibrary/"

for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        print(entry)


for root, dirs, files in os.walk(path):
    # Print the current directory path
    print(root)
