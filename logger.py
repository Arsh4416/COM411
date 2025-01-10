import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        """Logs a message with a timestamp to the log file."""
        try:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(self.log_file, 'a') as file:
                file.write(f"[{timestamp}] {message}\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")

    def log_error(self, error_message):
        """Logs an error message with a timestamp to the log file."""
        self.log(f"ERROR: {error_message}")

    def log_event(self, event_message):
        """Logs an event message with a timestamp to the log file."""
        self.log(f"EVENT: {event_message}")
