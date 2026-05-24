import sys
from gemini_service import get_comprehensive_report

def main():
    print("=============================================")
    print("      AI CAREER INTELLIGENCE PLATFORM       ")
    print("=============================================\n")
    
    while True:
        # Prompt user for input variables
        company = input("Enter Company Name (or type 'exit' to quit): ").strip()
        if company.lower() == 'exit':
            print("Exiting application. Goodbye!")
            break
            
        job = input("Enter Job Title: ").strip()
        
        if not company or not job:
            print("[Error] Both company and job title are required. Try again.\n")
            continue
            
        print(f"\n[Searching] Running deep lookup for {job} at {company}... Please wait.")
        
        try:
            # Call our separate module file logic
            report = get_comprehensive_report(company, job)
            
            # Print Formatted Report Layout
            print(f"\n================================================================")
            print(f" MASTER CAREER INTEL REPORT: {report.company_name.upper()} - {report.job_title.upper()}")
            print(f"================================================================\n")
            
            print(f"--- 1. OVERALL EMPLOYEE REVIEW & EXPERIENCE ---")
            print(f"• WLB Insight: {report.review_section.wlb_rating}")
            print(f"• Career Track: {report.review_section.career_growth}")
            print("\n✔ Pros:")
            for pro in report.review_section.pros: print(f"  + {pro}")
            print("\n✘ Cons:")
            for con in report.review_section.cons: print(f"  - {con}")
                
            print(f"\n--- 2. COMPENSATION & REWARDS BREAKDOWN ---")
            print(f"• Base Salary Structure: {report.salary_section.base_salary_range}")
            print(f"• Bonus & Equity Tranches: {report.salary_section.bonus_and_equity}")
            print("\n• Core Corporate Perks:")
            for perk in report.salary_section.benefits_highlights: print(f"  * {perk}")
                
            print(f"\n--- 3. END-TO-END INTERVIEW PIPELINE INTERCEPT ---")
            print(f"• Strategy & Difficulty: {report.interview_section.difficulty_and_tips}")
            print("\n• Pipeline Stages:")
            for step in report.interview_section.stages: print(f"  {step}")
            print("\n• Target Interview Questions Gathered:")
            for question in report.interview_section.common_questions: print(f"  ? \"{question}\"")
            print(f"\n================================================================\n")
            
        except Exception as e:
            print(f"\n[Error] Could not retrieve data: {e}\n")

if __name__ == "__main__":
    main()