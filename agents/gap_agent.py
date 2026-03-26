class GapAgent:
    def find(self, jd_skills, resume_skills):
        return list(set(jd_skills) - set(resume_skills))