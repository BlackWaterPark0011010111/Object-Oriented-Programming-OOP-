import re

class LogParser:

    def __init__(self, log_file):
        self.log_file = log_file

    def extract_messages(self):
        """Читает лог-файл и вытаскивает текст сообщений  //Reads the log file and extracts the text of the messages"""
        pattern = re.compile(r"\[(INFO|WARNING|ERROR)\] (.+)")
        messages = []

        with open(self.log_file, "r", encoding="utf-8") as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    messages.append((match.group(1), match.group(2)))

        return messages