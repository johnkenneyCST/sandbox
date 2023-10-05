from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import sys 
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print("New file created:", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File Deleted: {event.src_path}")

    


if __name__ == "__main__":
    print("Started")
    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, path='./scripts', recursive=False)
    observer.start()
    iteration = 1
    try:
        while True:
            print(f"Observing{'.'*iteration}")
            time.sleep(1.5)
            os.system("cls")
            iteration += 1
            if iteration >= 15:
                iteration = 1
    except KeyboardInterrupt:
        observer.stop()
        
    observer.join()