import objc
import Photos

# Get the shared Photos library
library = Photos.PHPhotoLibrary.shared()

# Fetch the list of all albums in the library
albums = library.getAlbums(options=None)

# Iterate over the albums and print their names
for album in albums:
    print(album.localizedTitle)

# Fetch the list of all smart albums in the library
smart_albums = library.getSmartAlbums(options=None)

# Iterate over the smart albums and print their names
for smart_album in smart_albums:
    print(smart_album.localizedTitle)

# Fetch the list of all moments in the library
moments = library.getMoments(options=None)

# Iterate over the moments and print their names
for moment in moments:
    print(moment.localizedTitle)

# Fetch the list of all people in the library
people = library.getPeople(options=None)

# Iterate over the people and print their names
for person in people:
    print(person.localizedFullName)

