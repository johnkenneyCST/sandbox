from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys 
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print("New file created:", event.src_path)


if __name__ == "__main__":
    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, path='./scripts', recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()