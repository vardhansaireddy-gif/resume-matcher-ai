from agents.parser_agent import ParserAgent
from agents.cleaning_agent import CleaningAgent
from agents.skill_agent import SkillAgent
from agents.jd_agent import JDAgent
from agents.tfidf_agent import TFIDFAgent
from agents.similarity_agent import SimilarityAgent
from agents.gap_agent import GapAgent
from agents.recommendation_agent import RecommendationAgent

class Coordinator:
    def __init__(self):
        self.parser = ParserAgent()
        self.cleaner = CleaningAgent()
        self.skill = SkillAgent()
        self.jd = JDAgent()
        self.tfidf = TFIDFAgent()
        self.similarity = SimilarityAgent()
        self.gap = GapAgent()
        self.recommend = RecommendationAgent()

    def run(self, resume_file, job_desc):
        resume_text = self.parser.parse(resume_file)
        clean_resume = self.cleaner.clean(resume_text)

        jd_text = self.jd.process(job_desc)

        resume_skills = self.skill.extract(clean_resume)
        jd_skills = self.skill.extract(jd_text)

        vectors = self.tfidf.vectorize(clean_resume, jd_text)
        score = self.similarity.compute(vectors)

        gaps = self.gap.find(jd_skills, resume_skills)
        suggestions = self.recommend.suggest(gaps)

        return score, gaps, suggestions