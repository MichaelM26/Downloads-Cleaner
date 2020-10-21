from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import json

class myHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            
            if src.endswith('.exe'):
                myHandler()
                folder_destination = "/Users/micha/Documents/Downloads/Executables"
            elif src.endswith(tuple(img)):
                myHandler()
                folder_destination = "/Users/micha/Documents/Downloads/Images"
            elif src.endswith(tuple(txt)):
                myHandler()
                folder_destination = "/Users/micha/Documents/Downloads/Text"
            else:
                myHandler()
                folder_destination = "/Users/micha/Documents/Downloads/Other"

            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

img = ['.jpg', '.png', '.jpeg', '.gif']
txt = ['.docx', '.doc', '.txt', '.pdf']

folder_to_track = "/Users/micha/Downloads"

event_handler = myHandler()
Observer = Observer()
Observer.schedule(event_handler, folder_to_track, recursive = True)
Observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    Observer.stop()
Observer.join()