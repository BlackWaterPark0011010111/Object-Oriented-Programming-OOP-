from collections import Counter

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_dict = {
            "ERROR": -1,  # Плохие новости  Bad News
            "WARNING": 0,  # Нейтральные  Neutral
            "INFO": 1      # Всё хорошо  its all good
        }

    def analyze(self, messages):
        """Анализирует частоту разных типов логов    Analyzes the frequency of different types of logs"""
        sentiments = [self.sentiment_dict.get(level, 0) for level, _ in messages]
        count = Counter(sentiments)

        total = sum(count.values())
        mood_score = sum(level * count[level] for level in count) / total if total else 0

        return mood_score