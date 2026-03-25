import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

class CleaningAgent:
    def clean(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z ]', '', text)
        words = text.split()
        words = [w for w in words if w not in stopwords.words('english')]
        return " ".join(words)