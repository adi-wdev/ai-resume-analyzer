from hybrid_matcher import calculate_hybrid_match


def compare_multiple_jobs(resume_text, jobs):

    results = []

    # Handle empty job list
    if not jobs:
        return {
            "total_jobs_analyzed": 0,
            "best_match": None,
            "job_rankings": [],
            "recommended_jobs": []
        }

    # Compare resume against every job
    for job in jobs:

        job_title = job["job_title"]
        job_description = job["job_description"]

        result = calculate_hybrid_match(
            resume_text,
            job_description
        )

        results.append({
            "job_title": job_title,
            "hybrid_score": result["hybrid_score"],
            "category": result["category"],
            "matched_skills": result["matched_skills"],
            "missing_skills": result["missing_skills"],
            "recommendation": result["recommendation"]
        })

    # Sort jobs by hybrid score
    results.sort(
        key=lambda x: x["hybrid_score"],
        reverse=True
    )

    # Assign rankings
    for index, result in enumerate(results, start=1):
        result["rank"] = index

    # Find best matching job
    best_match = results[0] if results else None

    # Filter jobs with score >= 50%
    recommended_jobs = [
        job for job in results
        if job["hybrid_score"] >= 50
    ]

    return {
        "total_jobs_analyzed": len(results),
        "best_match": best_match,
        "job_rankings": results,
        "recommended_jobs": recommended_jobs
    }