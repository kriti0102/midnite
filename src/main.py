import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from processor import process_bet_file

WATCH_DIR = "/opt/src/landed_files"

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class BetFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".csv"):
            time.sleep(1)  # slight delay in case file is still being written
            process_bet_file(event.src_path)

if __name__ == "__main__":
    logging.info(f"👀 Watching for new files in: {WATCH_DIR}")
    observer = Observer()
    event_handler = BetFileHandler()
    observer.schedule(event_handler, path=WATCH_DIR, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("👋 File watcher stopped.")
    observer.join()
