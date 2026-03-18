# screening logic

from resume_parser import extract_skills, extract_experience

def screen_resume(resume_text, required_skill):
    skills = extract_skills(resume_text)
    exp = extract_experience(resume_text)

    score = 0

    if required_skill in skills:
        score += 10

    score += exp

    return {
        "skills": skills,
        "experience": exp,
        "score": score
    }
