from text_similarity import calculate_text_similarity

resume = """
I am a Java developer.
I have experience with Spring Boot.
I develop backend applications and REST APIs.
"""

job_description = """
We are looking for a Java developer.
Experience with Spring Boot is required.
The candidate should develop backend applications and REST APIs.
"""

result = calculate_text_similarity(resume, job_description)

print("Similarity:", result["similarity_percentage"], "%")
print("Category:", result["category"])