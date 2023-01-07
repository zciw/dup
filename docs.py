import os
import sys
from AppKit import *
from Foundation import *

p = '/Users/zciw/Pictures/Biblioteka Zdjęć.photoslibrary'

app = NSApplication.sharedApplication()
notification_center = NSDistributedNotificationCenter.defaultCenter()

notification_center.addObserver_selector_name_object_(app, "createNote:", "com.apple.Scripting.noteCreationNotification", None)

def createNote(self, notification):
    user_info = notification.userInfo()
    note_text = user_info["note text"]
    note_subject = user_info["note subject"]
    note_attachments = user_info["note attachments"]

    notes_app = SBApplication.applicationWithBundleIdentifier_("com.apple.Notes")
    new_note = notes_app.Classes.__getitem__("note").alloc().init()
    new_note.title = note_subject
    new_note.content = note_text
    for attachment in note_attachments:
        new_note.addAttachment_(attachment)
    notes_app.currentFolder.notes.addObject_(new_note)

count=0
tagged_photos = []
for root, dirs, files in os.walk(p):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".raw"):
            file_path = os.path.join(root, file)
            count = count + 1
            tags = os.popen(f"mdls -name kMDItemUserTags {file_path}").read()
            if "tagged" in tags:
                tagged_photos.append(file_path)

print(f'tagged:  {len(tagged_photos)}, from {count}')

# verImmediately_("com.apple.Scripting.noteCreationNotification", None, {"note subject": "Tagged Photos", "note text": "", "note attachments": tagged_photos}, True)
