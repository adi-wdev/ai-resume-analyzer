import re


def check_ats_compatibility(resume_text):

    # Assignment 1: Handle empty resume
    if not resume_text or not resume_text.strip():
        return {
            "message": "Resume text cannot be empty.",
            "ats_score": 0,
            "category": "Not Analyzed",
            "checks_passed": [],
            "total_checks_passed": 0,
            "score_breakdown": {},
            "suggestions": [
                "Please provide your resume text for ATS analysis."
            ]
        }

    text = resume_text.lower()

    score = 0
    checks = []
    suggestions = []

    score_breakdown = {}

    # 1. Contact Information - 20 points

    email_pattern = (
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    )

    # Assignment 2: Support multiple Indian phone formats
    phone_pattern = (
        r"(?<!\d)(?:\+91[-.\s]?)?[6-9]\d{9}(?!\d)"
    )

    has_email = re.search(email_pattern, resume_text)
    has_phone = re.search(phone_pattern, resume_text)

    if has_email and has_phone:
        score += 20
        score_breakdown["contact_information"] = 20
        checks.append("Email and phone number found.")
    else:
        score_breakdown["contact_information"] = 0

        if not has_email:
            suggestions.append("Add a valid email address.")

        if not has_phone:
            suggestions.append("Add a valid phone number.")

        checks.append("Contact information is incomplete.")

    # 2. Skills Section - 20 points

    if re.search(r"\bskills\b", text):
        score += 20
        score_breakdown["skills"] = 20
        checks.append("Skills section found.")
    else:
        score_breakdown["skills"] = 0
        suggestions.append("Add a clearly labelled Skills section.")

    # 3. Education Section - 20 points

    if re.search(r"\beducation\b", text):
        score += 20
        score_breakdown["education"] = 20
        checks.append("Education section found.")
    else:
        score_breakdown["education"] = 0
        suggestions.append("Add an Education section.")

    # 4. Experience Section - 20 points

    experience_headings = [
        "experience",
        "work experience",
        "professional experience",
        "internship"
    ]

    has_experience = any(
        heading in text
        for heading in experience_headings
    )

    if has_experience:
        score += 20
        score_breakdown["experience"] = 20
        checks.append("Experience section found.")
    else:
        score_breakdown["experience"] = 0
        suggestions.append(
            "Add an Experience or Internship section."
        )

    # 5. Projects Section - 10 points

    if re.search(r"\bprojects?\b", text):
        score += 10
        score_breakdown["projects"] = 10
        checks.append("Projects section found.")
    else:
        score_breakdown["projects"] = 0
        suggestions.append("Add a Projects section.")

    # 6. Action Words - 10 points

    action_words = [
        "developed",
        "implemented",
        "created",
        "designed",
        "improved",
        "managed",
        "built"
    ]

    has_action_words = any(
        word in text
        for word in action_words
    )

    if has_action_words:
        score += 10
        score_breakdown["action_words"] = 10
        checks.append("Action-oriented words found.")
    else:
        score_breakdown["action_words"] = 0
        suggestions.append(
            "Use action words such as developed, implemented and created."
        )

    # Assignment 3: Professional Summary Section

    has_summary = (
        re.search(r"\bsummary\b", text)
        or "professional summary" in text
    )

    if has_summary:
        checks.append("Professional summary section found.")
    else:
        suggestions.append(
            "Add a professional summary highlighting your "
            "experience, technical strengths and career goals."
        )

    # Calculate ATS category

    if score >= 80:
        category = "Excellent"
    elif score >= 60:
        category = "Good"
    elif score >= 40:
        category = "Moderate"
    else:
        category = "Needs Improvement"

    return {
        "message": "ATS compatibility check completed successfully.",
        "ats_score": score,
        "category": category,
        "checks_passed": checks,
        "total_checks_passed": len(checks),
        "score_breakdown": score_breakdown,
        "suggestions": suggestions
    }