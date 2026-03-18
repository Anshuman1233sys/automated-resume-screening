# simple resume parser (dummy logic)

def extract_skills(resume_text):
    skills_list = ["python", "java", "sql", "ml", "data analysis"]
    found_skills = []

    for skill in skills_list:
        if skill in resume_text.lower():
            found_skills.append(skill)

    return found_skills


def extract_experience(resume_text):
    # dummy logic for experience
    if "3 years" in resume_text:
        return 3
    elif "2 years" in resume_text:
        return 2
    else:
        return 1
