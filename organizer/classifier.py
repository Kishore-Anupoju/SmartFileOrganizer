import json
import os


class FileClassifier:

    def __init__(self, config_path):

        with open(config_path, "r") as file:
            self.config = json.load(file)

    def classify(self, filename):

        extension = os.path.splitext(filename)[1].lower()

        return self.config["categories"].get(
            extension,
            self.config["default_category"]
        )