from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os


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

        filename = os.path.basename(
            source_path
        )

        category = self.classifier.classify(
            filename
        )

        destination_folder = os.path.join(
            self.watch_folder,
            category
        )

        new_location = self.mover.move_file(
            source_path,
            destination_folder
        )

        message = (
            f"{filename} -> {category}"
        )

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