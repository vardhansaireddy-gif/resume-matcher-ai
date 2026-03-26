from sklearn.metrics.pairwise import cosine_similarity

class SimilarityAgent:
    def compute(self, vectors):
        score = cosine_similarity(vectors[0:1], vectors[1:2])
        return float(score[0][0]) * 100