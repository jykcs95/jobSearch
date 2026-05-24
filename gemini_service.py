import os
from google import genai
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# --- DATA STRUCTURES ---

#Prompting Review
class DeepReview(BaseModel):
    pros: list[str] = Field(description="3 distinct advantages like culture, WFH, or tech stack.")
    cons: list[str] = Field(description="3 distinct downsides like lack of promotion or burnout.")
    wlb_rating: str = Field(description="Detailed evaluation of Work-Life Balance and weekly hours.")
    career_growth: str = Field(description="Breakdown of promotion velocity and internal mobility.")

#Prompting Salary
class DeepSalary(BaseModel):
    base_salary_range: str = Field(description="Accurate base pay spread for this title.")
    bonus_and_equity: str = Field(description="Detailed breakdown of signing bonuses, performance cash, and stock.")
    benefits_highlights: list[str] = Field(description="Notable perks specific to this company.")

#Prompting Interview
class DeepInterview(BaseModel):
    stages: list[str] = Field(description="Chronological step-by-step pipeline stages.")
    common_questions: list[str] = Field(description="3 specific interview questions asked for this role.")
    difficulty_and_tips: str = Field(description="Perceived difficulty level and preparation strategies.")

#Add all the prompts together
class ComprehensiveJobReport(BaseModel):
    company_name: str
    job_title: str
    review_section: DeepReview
    salary_section: DeepSalary
    interview_section: DeepInterview

# --- Define Core Lookup Function ---

#Change Gemini to a company intelligence focused
def get_comprehensive_report(company: str, job: str) -> ComprehensiveJobReport:
    client = genai.Client()
    
    #Giving Gemini the roles and detailed search its going to do
    prompt = f"""
    You are an elite corporate recruiter and career intelligence analyst. 
    Conduct an exhaustive, deep-dive investigation into the '{job}' position at '{company}'.
    
    Synthesize your knowledge to act as a replacement for three individual deep-web searches:
    1. A complete Glassdoor/Reddit analysis of employee reviews, cultural benefits, and work-life balance realities.
    2. A comprehensive Levels.fyi salary lookup detailing base compensation, equity tranches, and performance bonuses.
    3. An end-to-end interview prep post covering the exact pipeline structure, test types, and specific real-world screening questions.
    
    Provide concrete data, clear numbers, and realistic breakdowns. Do not use generic filler text.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': ComprehensiveJobReport,
        }
    )
    
    return ComprehensiveJobReport.model_validate_json(response.text)