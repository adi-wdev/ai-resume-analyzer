from job_matcher import calculate_match


def generate_resume_improvements(resume_text, job_description):

    # Analyze resume against job description
    match_result = calculate_match(
        resume_text,
        job_description
    )

    required_skills = match_result["required_skills"]

    if not required_skills:
        return {
            "match_score": 0,
            "missing_skills": [],
            "total_improvements": 1,
            "summary": "No recognizable technical skills found in the job description.",
            "improvements": [
                {
                    "area": "Job Description",
                    "issue": "No recognizable technical skills were detected.",
                    "suggestion": (
                        "Please provide a job description containing "
                        "specific technical skills."
                    )
                }
            ]
        }

    missing_skills = match_result["missing_skills"]

    improvements = []

    # 1. Missing skills
    if missing_skills:
        improvements.append({
            "area": "Technical Skills",
            "issue": "Some required skills are missing from your resume.",
            "suggestion": (
                "If you genuinely have experience with these skills, "
                "include them with relevant examples: "
                + ", ".join(missing_skills)
            )
        })

    # 2. Resume length
    if len(resume_text.split()) < 100:
        improvements.append({
            "area": "Resume Content",
            "issue": "Your resume contains very little information.",
            "suggestion": (
                "Add relevant education, projects, technical skills "
                "and practical experience."
            )
        })

    # 3. Measurable achievements
    achievement_words = [
        "increased",
        "reduced",
        "improved",
        "developed",
        "implemented",
        "optimized"
    ]

    has_achievements = any(
        word in resume_text.lower()
        for word in achievement_words
    )

    if not has_achievements:
        improvements.append({
            "area": "Achievements",
            "issue": "Your resume may lack strong achievement statements.",
            "suggestion": (
                "Describe what you built or improved. "
                "Include measurable results when you have evidence."
            )
        })

    # 4. Projects
    if "project" not in resume_text.lower():
        improvements.append({
            "area": "Projects",
            "issue": "No project-related information was detected.",
            "suggestion": (
                "Add relevant projects describing their technologies, "
                "your contribution and the results."
            )
        })

    # 5. Education check
    if "education" not in resume_text.lower():
        improvements.append({
            "area": "Education",
            "issue": "Education information was not detected.",
            "suggestion": (
                "Add your educational qualifications, degree, "
                "institution and graduation year."
            )
        })

    # Final summary
    if not improvements:
        summary = "Your resume looks good based on these basic checks."
    else:
        summary = (
            "Your resume has "
            + str(len(improvements))
            + " areas that could be improved."
        )

    return {
        "match_score": match_result["match_score"],
        "missing_skills": missing_skills,
        "total_improvements": len(improvements),
        "summary": summary,
        "improvements": improvements
    }