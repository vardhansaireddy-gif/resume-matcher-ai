class SkillAgent:
    SKILLS = [
        "python", "java", "c++", "machine learning",
        "deep learning", "nlp", "sql", "tensorflow",
        "pytorch", "data analysis"
    ]

    def extract(self, text):
        found = []
        for skill in self.SKILLS:
            if skill in text:
                found.append(skill)
        return found