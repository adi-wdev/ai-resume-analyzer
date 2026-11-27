from job_matcher import calculate_match
from text_similarity import calculate_text_similarity


def calculate_hybrid_match(resume_text, job_description):

    # Skill-based matching
    skill_result = calculate_match(
        resume_text,
        job_description
    )

    skill_score = skill_result["match_score"]

    # Text similarity
    text_result = calculate_text_similarity(
        resume_text,
        job_description
    )

    text_score = text_result["similarity_percentage"]

    # Hybrid score
    hybrid_score = (
        skill_score * 0.7
        + text_score * 0.3
    )

    hybrid_score = round(hybrid_score, 2)

    # Assign category
    if hybrid_score >= 80:
        category = "Excellent Match"

    elif hybrid_score >= 60:
        category = "Good Match"

    elif hybrid_score >= 40:
        category = "Moderate Match"

    else:
        category = "Low Match"

    return {
        "skill_score": skill_score,
        "text_similarity_score": text_score,
        "hybrid_score": hybrid_score,
        "category": category
    }