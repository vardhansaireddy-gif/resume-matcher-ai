class RecommendationAgent:
    def suggest(self, gaps):
        suggestions = []
        for skill in gaps:
            suggestions.append(f"Consider learning {skill}")
        return suggestions