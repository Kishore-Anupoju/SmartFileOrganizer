from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time


def is_temp_file(filename):
    temp_patterns = [
        ".crdownload",
        ".tmp",
        ".part",
        ".com.google.Chrome"
    ]

    return any(pattern in filename for pattern in temp_patterns)


def wait_until_file_stable(path, wait_time=2):
    try:
        initial_size = os.path.getsize(path)
        time.sleep(wait_time)
        final_size = os.path.getsize(path)
        return initial_size == final_size
    except Exception:
        return False


class DownloadWatcher(FileSystemEventHandler):

    def __init__(
        self,
        classifier,
        mover,
        logger,
        watch_folder
    ):
        self.classifier = classifier
        self.mover = mover
        self.logger = logger
        self.watch_folder = watch_folder

    def on_created(self, event):

        if event.is_directory:
            return

        source_path = event.src_path

        filename = os.path.basename(source_path)

        # ==============================
        # 🔥 FIX 1: Ignore temp files
        # ==============================
        if is_temp_file(filename):
            print(f"Ignoring temporary file: {filename}")
            return

        # ==============================
        # 🔥 FIX 2: Wait until download completes
        # ==============================
        if not wait_until_file_stable(source_path):
            print(f"File still downloading, skipping: {filename}")
            return

        # ==============================
        # Existing logic (safe now)
        # ==============================
        category = self.classifier.classify(filename)

        destination_folder = os.path.join(
            self.watch_folder,
            category
        )

        new_location = self.mover.move_file(
            source_path,
            destination_folder
        )

        message = f"{filename} -> {category}"

        self.logger.log(message)

        print(message)


def start_watcher(
    watch_folder,
    classifier,
    mover,
    logger
):

    observer = Observer()

    handler = DownloadWatcher(
        classifier,
        mover,
        logger,
        watch_folder
    )

    observer.schedule(
        handler,
        watch_folder,
        recursive=False
    )

    observer.start()

    return observer