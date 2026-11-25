from skill_extractor import extract_skills


def analyze_job_description(job_description):

    required_skills = extract_skills(job_description)

    return {
        "required_skills": required_skills,
        "total_required_skills": len(required_skills)
    }


def calculate_match(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    resume_set = set(resume_skills)
    required_set = set(required_skills)

    matched_skills = resume_set.intersection(required_set)
    missing_skills = required_set - resume_set

    if len(required_set) == 0:
        match_score = 0
    else:
        match_score = (
            len(matched_skills) / len(required_set)
        ) * 100

    return {
        "resume_skills": sorted(resume_set),
        "required_skills": sorted(required_set),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "match_score": round(match_score, 2)
    }