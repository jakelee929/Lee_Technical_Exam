import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from processor import process_file

WATCH_DIR = "storage/app/medalists"

class MedalistHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".csv"):
            process_file(event.src_path)

def start_watching():
    observer = Observer()
    observer.schedule(MedalistHandler(), WATCH_DIR, recursive=False)
    observer.start()
    print("Watching for new files...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watching()
