from hybrid_matcher import calculate_hybrid_match

resume = """
I am a Java developer.
I have experience with Spring Boot.
I develop REST APIs using Java.
I have worked with PostgreSQL.
I also know HTML and CSS.
"""

job_description = """
We need a Java developer with Spring Boot experience.
The candidate should develop REST APIs.
Knowledge of PostgreSQL, Python and Docker is required.
"""

result = calculate_hybrid_match(
    resume,
    job_description
)

print("\n===== HYBRID MATCH REPORT =====")

print("Skill Score:", result["skill_score"])
print("Text Similarity:", result["text_similarity_score"])
print("Hybrid Score:", result["hybrid_score"])
print("Category:", result["category"])

print("\nMatched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])
print("Extra Skills:", result["extra_skills"])

print("\nExplanation:")

for explanation in result["explanations"]:
    print("-", explanation)