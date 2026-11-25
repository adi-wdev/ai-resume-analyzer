
from fastapi import FastAPI
from pydantic import BaseModel, Field
from skill_extractor import extract_skills, categorize_skills

app = FastAPI(
    title="AI Resume Analyzer",
    description="Python AI service for resume analysis",
    version="1.0.0"
)


# Request Model
class ResumeAnalysisRequest(BaseModel):
    resume_text: str = Field(min_length=1)
    job_description: str = Field(min_length=1)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer AI Service",
        "status": "Running"
    }


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


@app.get("/about")
def about():
    return {
        "project": "AI Resume Analyzer",
        "developer": "Kumar Aditya",
        "technology": "Python and FastAPI",
        "version": "1.0"
    }
