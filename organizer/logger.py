from datetime import datetime


class ActivityLogger:

    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.log_file, "a") as file:
            file.write(f"[{timestamp}] {message}\n")