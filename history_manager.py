import pandas as pd

class HistoryManager:
    def __init__(self, history_file='history.csv'):
        self.history_file = history_file
        try:
            self.history = pd.read_csv(history_file)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=["operation", "result"])

    def add_history(self, operation, result):
        new_entry = pd.DataFrame([[operation, result]], columns=["operation", "result"])
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.save_history()

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=["operation", "result"])
        self.save_history()

    def get_history(self):
        return self.history

