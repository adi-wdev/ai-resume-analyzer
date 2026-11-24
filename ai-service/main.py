from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI Resume Analyzer",
    description="Python AI service for resume analysis",
    version="1.0.0"
)


class ResumeAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str


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

    return {
        "message": "Resume received successfully",
        "resume_word_count": len(resume_words),
        "job_description_word_count": len(job_words)
    }