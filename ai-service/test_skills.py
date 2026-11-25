from skill_extractor import extract_skills

resume = """
I know Java, Python, SpringBoot, ReactJS,
Machine Learning, SQL, and AWS.
"""

skills = extract_skills(resume)

print("Extracted Skills:", skills)