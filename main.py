# automated resume screening (basic)

resumes = [
    {"name": "Aman", "skills": ["python", "ml"], "exp": 2},
    {"name": "Riya", "skills": ["java", "sql"], "exp": 1},
    {"name": "Rahul", "skills": ["python", "data"], "exp": 3}
]

filtered = []

for r in resumes:
    if "python" in r["skills"]:
        filtered.append(r)

filtered = sorted(filtered, key=lambda x: x["exp"], reverse=True)

print("Shortlisted Candidates:")
for i in filtered:
    print(i["name"], "-", i["exp"])
