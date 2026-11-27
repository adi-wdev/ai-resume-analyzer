from multi_job_matcher import compare_multiple_jobs


resume = """
I am a Java developer.
I have experience with Spring Boot.
I develop REST APIs.
I know Python and PostgreSQL.
I have basic knowledge of Machine Learning.
"""


jobs = [

    {
        "job_title": "Java Developer",
        "job_description": """
        Java, Spring Boot, PostgreSQL and REST APIs required.
        """
    },

    {
        "job_title": "Python Developer",
        "job_description": """
        Python, Django and MySQL required.
        """
    },

    {
        "job_title": "Full Stack Developer",
        "job_description": """
        Java, React, Node.js and CSS required.
        """
    },

    {
        "job_title": "Data Analyst",
        "job_description": """
        Python, SQL, Excel, Power BI and statistics required.
        """
    },

    {
        "job_title": "Machine Learning Engineer",
        "job_description": """
        Python, Machine Learning, TensorFlow,
        PyTorch and SQL required.
        """
    }

]


result = compare_multiple_jobs(resume, jobs)


print("\n===== MULTIPLE JOB COMPARISON =====")

print("Total Jobs Analyzed:",
      result["total_jobs_analyzed"])


print("\n===== JOB RANKINGS =====")

for job in result["job_rankings"]:

    print("\nRank:", job["rank"])
    print("Job:", job["job_title"])
    print("Hybrid Score:", job["hybrid_score"], "%")
    print("Category:", job["category"])
    print("Matched Skills:", job["matched_skills"])
    print("Missing Skills:", job["missing_skills"])
    print("Recommendation:", job["recommendation"])


print("\n===== BEST MATCH =====")

if result["best_match"]:
    print(result["best_match"]["job_title"])


print("\n===== RECOMMENDED JOBS (50% OR ABOVE) =====")

for job in result["recommended_jobs"]:

    print(
        job["job_title"],
        "-",
        job["hybrid_score"],
        "%"
    )