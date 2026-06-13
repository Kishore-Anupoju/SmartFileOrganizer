import os
import shutil


class FileMover:

    def move_file(self, source_path, destination_folder):

        os.makedirs(
            destination_folder,
            exist_ok=True
        )

        filename = os.path.basename(
            source_path
        )

        destination_path = os.path.join(
            destination_folder,
            filename
        )

        shutil.move(
            source_path,
            destination_path
        )

        return destination_path