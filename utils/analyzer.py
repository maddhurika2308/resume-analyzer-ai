from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume, job_desc):
    texts = [resume, job_desc]
    
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(texts)
    
    similarity = cosine_similarity(matrix)[0][1]
    
    return round(similarity * 100, 2)
def extract_skills(text):
    skills_list = [
        "python", "java", "c++", "sql", "machine learning",
        "data analysis", "html", "css", "javascript",
        "react", "node", "deep learning", "ai"
    ]
    
    found_skills = []
    
    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    
    return found_skills
def get_missing_skills(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))
