# main app file

from screening import screen_resume

resumes = [
    "Aman has python and ml experience of 2 years",
    "Riya knows java and sql with 1 years experience",
    "Rahul has python and data analysis with 3 years"
]

results = []

for r in resumes:
    result = screen_resume(r, "python")
    results.append(result)

# sorting based on score
results = sorted(results, key=lambda x: x["score"], reverse=True)

print("Final Results:")
for r in results:
    print(r)
