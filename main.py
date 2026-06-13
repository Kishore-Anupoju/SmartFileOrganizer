from pathlib import Path
import time

from organizer.classifier import FileClassifier
from organizer.logger import ActivityLogger
from organizer.mover import FileMover
from organizer.watcher import start_watcher


watch_folder = str(
    Path.home() / "Downloads"
)

classifier = FileClassifier(
    "config.json"
)

logger = ActivityLogger(
    "logs/history.log"
)

mover = FileMover()

observer = start_watcher(
    watch_folder,
    classifier,
    mover,
    logger
)

print(
    f"Smart File Organizer running..."
)

try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    observer.stop()

observer.join()