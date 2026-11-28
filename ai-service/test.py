from ats_checker import check_ats_compatibility

resume = """
Email: test@example.com
Phone: 9876543210

EDUCATION
B.Tech Computer Science

SKILLS
Java, Python, SQL

PROJECTS
AI Resume Analyzer

Developed a resume matching application.
"""

result = check_ats_compatibility(resume)

print("ATS Score:", result["ats_score"])

print("\nScore Breakdown:")

for category, points in result["score_breakdown"].items():
    print(category, ":", points)

print("\nSuggestions:")
for suggestion in result["suggestions"]:
    print("-", suggestion)