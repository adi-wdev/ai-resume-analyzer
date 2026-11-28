
from fastapi import FastAPI
from pydantic import BaseModel, Field
from skill_extractor import extract_skills, categorize_skills
from job_matcher import calculate_match
from evidence_extractor import extract_skill_evidence
from text_similarity import calculate_text_similarity
from hybrid_matcher import calculate_hybrid_match
from learning_recommender import generate_learning_roadmap
from resume_improver import generate_resume_improvements
from ats_checker import check_ats_compatibility
from fastapi import UploadFile, File, HTTPException
from pdf_parser import extract_text_from_pdf
from skill_extractor import extract_skills

app = FastAPI(
    title="AI Resume Analyzer",
    description="Python AI service for resume analysis",
    version="1.0.0"
)


# Request Model
class ResumeAnalysisRequest(BaseModel):
    resume_text: str = Field(min_length=1)
    job_description: str = Field(min_length=1)

class ResumeEvidenceRequest(BaseModel):
    resume_text: str = Field(min_length=1)

class JobDescription(BaseModel):
    job_title: str = Field(min_length=1)
    job_description: str = Field(min_length=1)


class MultipleJobComparisonRequest(BaseModel):
    resume_text: str = Field(min_length=1)
    jobs: list[JobDescription] = Field(min_length=1)

class LearningRoadmapRequest(BaseModel):
    missing_skills: list[str]

class ResumeImprovementRequest(BaseModel):
    resume_text: str = Field(min_length=1)
    job_description: str = Field(min_length=1)

class ATSCheckRequest(BaseModel):
    resume_text: str = Field(min_length=1)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer AI Service",
        "status": "Running"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    # Assignment 1: Validate file extension
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    pdf_bytes = await file.read()

    # Assignment 3: Validate file size
    if len(pdf_bytes) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="PDF file size cannot exceed 5 MB."
        )

    try:
        # Extract text from PDF
        result = extract_text_from_pdf(pdf_bytes)

        extracted_text = result["extracted_text"]

        # Assignment 4: Extract skills automatically
        extracted_skills = extract_skills(extracted_text)

        return {
            "message": result["message"],
            "filename": file.filename,
            "total_pages": result["total_pages"],
            "character_count": result["character_count"],
            "extracted_text": extracted_text,
            "extracted_skills": extracted_skills,
            "total_skills": len(extracted_skills)
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    finally:
        await file.close()


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Resume Analyzer"
    }


@app.post("/analyze")
def analyze_resume(request: ResumeAnalysisRequest):

    resume_words = request.resume_text.split()
    job_words = request.job_description.split()

    skills = extract_skills(request.resume_text)

    return {
        "message": "Resume analyzed successfully",
        "resume_word_count": len(resume_words),
        "job_description_word_count": len(job_words),
        "resume_character_count": len(request.resume_text),
        "job_description_character_count": len(request.job_description),
        "extracted_skills": skills,
        "skill_categories": categorize_skills(skills)
    }


@app.post("/extract-skills")
def extract_resume_skills(request: ResumeAnalysisRequest):

    skills = extract_skills(request.resume_text)

    return {
        "message": "Skills extracted successfully",
        "skills": skills,
        "total_skills": len(skills),
        "skill_categories": categorize_skills(skills)
    }

@app.post("/extract-evidence")
def extract_evidence(request: ResumeEvidenceRequest):

    evidence = extract_skill_evidence(request.resume_text)

    return {
        "message": "Resume evidence extracted successfully",
        "evidence": evidence,
        "total_skills": len(evidence)
    }

@app.post("/analyze-match")
def analyze_match(request: ResumeAnalysisRequest):

    result = calculate_match(
        request.resume_text,
        request.job_description
    )

    return {
        "message": "Resume analysis completed successfully",
        "analysis": result
    }

@app.post("/hybrid-match")
def hybrid_match(request: ResumeAnalysisRequest):

    result = calculate_hybrid_match(
        request.resume_text,
        request.job_description
    )

    return {
        "message": "Hybrid resume matching completed successfully",
        "analysis": result
    }

@app.post("/text-similarity")
def text_similarity(request: ResumeAnalysisRequest):

    result = calculate_text_similarity(
        request.resume_text,
        request.job_description
    )

    return {
        "message": "Text similarity calculated successfully",
        "analysis": result
    }

@app.post("/compare-jobs")
def compare_jobs(request: MultipleJobComparisonRequest):

    jobs = [
        job.model_dump()
        for job in request.jobs
    ]

    result = compare_multiple_jobs(
        request.resume_text,
        jobs
    )

    return {
        "message": "Multiple job comparison completed successfully",
        "analysis": result
    }

@app.post("/learning-roadmap")
def learning_roadmap(request: LearningRoadmapRequest):

    result = generate_learning_roadmap(request.missing_skills)

    return {
        "message": "Learning roadmap generated successfully",
        "analysis": result
    }

@app.post("/improve-resume")
def improve_resume(request: ResumeImprovementRequest):

    result = generate_resume_improvements(
        request.resume_text,
        request.job_description
    )

    return {
        "message": "Resume improvement analysis completed successfully",
        "analysis": result
    }

@app.post("/check-ats")
def check_ats(request: ATSCheckRequest):

    result = check_ats_compatibility(
        request.resume_text
    )

    return {
        "message": "ATS compatibility check completed successfully",
        "analysis": result
    }

@app.get("/about")
def about():
    return {
        "project": "AI Resume Analyzer",
        "developer": "Kumar Aditya",
        "technology": "Python and FastAPI",
        "version": "1.0"
    }



def calculate_match(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    # Convert lists into sets to remove duplicates
    resume_set = set(resume_skills)
    required_set = set(required_skills)

    # Find matching and missing skills
    matched_skills = resume_set.intersection(required_set)
    missing_skills = required_set - resume_set

    # Calculate match percentage
    if len(required_set) == 0:
        match_score = 0
    else:
        match_score = (
            len(matched_skills) / len(required_set)
        ) * 100

    match_score = round(match_score, 2)

    # Assignment 1: Match category
    if match_score >= 80:
        category = "Excellent Match"
    elif match_score >= 60:
        category = "Good Match"
    elif match_score >= 40:
        category = "Moderate Match"
    else:
        category = "Low Match"

    # Assignment 2: Dynamic recommendation
    if len(required_set) == 0:
        recommendation = (
            "No recognizable skills were found in the job description. "
            "Unable to calculate a meaningful match."
        )

    elif len(missing_skills) == 0:
        recommendation = (
            "Excellent! Your resume contains all the required skills."
        )

    else:
        missing = ", ".join(sorted(missing_skills))

        recommendation = (
            f"Your resume matches {match_score}% of the required skills. "
            f"Consider learning {missing} to improve your compatibility "
            "with this position."
        )

    return {
        "resume_skills": sorted(resume_set),
        "required_skills": sorted(required_set),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "match_score": match_score,
        "category": category,
        "recommendation": recommendation
    }