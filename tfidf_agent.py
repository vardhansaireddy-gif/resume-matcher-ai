from sklearn.feature_extraction.text import TfidfVectorizer

class TFIDFAgent:
    def vectorize(self, resume, jd):
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume, jd])
        return vectors