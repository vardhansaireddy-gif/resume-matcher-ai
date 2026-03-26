class RankingAgent:
    def rank(self, scores):
        return sorted(scores, reverse=True)