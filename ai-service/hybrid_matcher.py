from job_matcher import calculate_match
from text_similarity import calculate_text_similarity


def calculate_hybrid_match(resume_text, job_description):

    # 1. Skill-based matching
    skill_result = calculate_match(
        resume_text,
        job_description
    )

    skill_score = skill_result["match_score"]

    matched_skills = skill_result["matched_skills"]
    missing_skills = skill_result["missing_skills"]
    extra_skills = skill_result.get("extra_skills", [])

    required_skills = skill_result["required_skills"]

    # 2. Text similarity
    text_result = calculate_text_similarity(
        resume_text,
        job_description
    )

    text_score = text_result["similarity_percentage"]

    # 3. Hybrid score
    hybrid_score = (
        skill_score * 0.7
        + text_score * 0.3
    )

    hybrid_score = round(hybrid_score, 2)

    # 4. Match category
    if hybrid_score >= 80:
        category = "Excellent Match"

    elif hybrid_score >= 60:
        category = "Good Match"

    elif hybrid_score >= 40:
        category = "Moderate Match"

    else:
        category = "Low Match"

    # 5. Skill match summary
    total_required = len(required_skills)
    total_matched = len(matched_skills)
    total_missing = len(missing_skills)

    # 6. Generate recommendation
    if total_required == 0:
        recommendation = (
            "No recognizable technical skills were found "
            "in the job description. Please provide more "
            "specific technical requirements."
        )

    elif missing_skills:
        recommendation = (
            "Learn " + " and ".join(missing_skills)
            + " to improve your job compatibility."
        )

    else:
        recommendation = (
            "You have all the required skills for this job."
        )

    # 7. Generate explanations
    explanations = []

    if total_required == 0:
        explanations.append(
            "No recognizable required skills were found."
        )

    else:
        explanations.append(
            f"You matched {total_matched} out of "
            f"{total_required} required skills."
        )

    if missing_skills:
        explanations.append(
            "Missing skills: " + ", ".join(missing_skills)
        )

    if extra_skills:
        explanations.append(
            "Additional skills: " + ", ".join(extra_skills)
        )

    explanations.append(
        f"Text similarity score: {text_score}%."
    )

    return {
        "skill_score": skill_score,
        "text_similarity_score": text_score,
        "hybrid_score": hybrid_score,
        "category": category,

        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "extra_skills": extra_skills,

        "skill_summary": {
            "total_required_skills": total_required,
            "total_matched_skills": total_matched,
            "total_missing_skills": total_missing
        },

        "recommendation": recommendation,
        "explanations": explanations
    }