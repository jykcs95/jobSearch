import streamlit as st
from gemini_service import get_comprehensive_report

# 1. Page Configuration & Styling
st.set_page_config(page_title="AI Career Intelligence", page_icon="💼", layout="wide")

st.html(
    """
    <style>
        /* Base text inside paragraphs, info boxes, and lists */
        p, li, span, .stText, label {
            font-size: 1.15rem !important; /* ~18px font size */
            line-height: 1.6 !important;
        }
        /* Metrics values (like your 1 to 5 company rating score) */
        [data-testid="stMetricValue"] {
            font-size: 2.5rem !important;
        }
        /* Tab titles at the top of your dashboard sections */
        button[data-baseweb="tab"] p {
            font-size: 1.25rem !important;
            font-weight: 600 !important;
        }
        /* Hide Enter Helper Text */
        [data-testid="stWidgetInstructions"], 
        [data-testid="InputInstructions"] {
            display: none !important;
            visibility: hidden !important;
            height: 0px !important;
        }
    </style>
    """
)

st.title("💼 AI Career Intelligence Platform")
st.markdown("Generate deep-dive corporate reports, salary distributions, and interview pipelines instantly.")
st.write("---")

# 2. Input Sidebar Panel
st.sidebar.header("📋 Search Parameters")
company = st.sidebar.text_input("Company Name", placeholder="e.g., Google").strip()
job = st.sidebar.text_input("Job Title", placeholder="e.g., Data Scientist").strip()
location = st.sidebar.text_input("Target Location (Optional)", placeholder="Default: Chicago").strip()

target_location = location if location else "Chicago"

# 3. Execution Trigger Button
if st.sidebar.button("Generate Intelligence Report", type="primary"):
    if not company or not job:
        st.sidebar.error("⚠️ Both Company Name and Job Title are strictly required.")
    else:
        with st.spinner(f"Conducting deep-web intelligence scan for {job} at {company}..."):
            try:
                report = get_comprehensive_report(company, job, target_location)
                st.success(f"Report Generated for {report.company_name}!")
                
                st.header(f"🏢 {report.company_name} — {report.job_title}")
                st.info(f"📍 Salary Geolocation Focus: **{target_location}** vs. **United States National Average**")
                
                tab1, tab2, tab3 = st.tabs(["📊 Employee Experience & Reviews", "💰 Compensation & Rewards", "🎯 Interview Pipeline Intercept"])
                
                # --- TAB 1: REVIEWS ---
                with tab1:
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.metric(label="Overall Employee Rating", value=f"⭐ {report.review_section.company_rating} / 5.0")
                    with col2:
                        st.markdown(f"**Work-Life Balance Realities:** {report.review_section.wlb_rating}")
                        st.markdown(f"**Career Velocity & Growth:** {report.review_section.career_growth}")
                    
                    st.write("---")
                    pro_col, con_col = st.columns(2)
                    with pro_col:
                        st.subheader("🟢 Cultural Pros")
                        for pro in report.review_section.pros: st.write(f"✅ {pro}")
                    with con_col:
                        st.subheader("🔴 Cultural Cons")
                        for con in report.review_section.cons: st.write(f"❌ {con}")

                # --- TAB 2: SALARY ---
                with tab2:
                    local_col, nat_col = st.columns(2)
                    with local_col:
                        st.markdown(f"### 📍 Local Market: {target_location.upper()}")
                        st.info(f"**Base Pay Scale:**\n{report.salary_section.location_specifics.base_salary_range}")
                        st.write(f"**Bonus & Stock Distribution:**\n{report.salary_section.location_specifics.bonus_and_equity}")
                    with nat_col:
                        st.markdown("### 🇺🇸 National Market Baseline")
                        st.warning(f"**Base Pay Scale:**\n{report.salary_section.national_specifics.base_salary_range}")
                        st.write(f"**Bonus & Stock Distribution:**\n{report.salary_section.national_specifics.bonus_and_equity}")
                    st.write("---")

                    st.subheader("🎁 Corporate Perks & Health Benefits")
                    for perk in report.salary_section.benefits_highlights:
                        st.markdown(f"🌟 {perk}")

                # --- TAB 3: INTERVIEWS ---
                with tab3:
                    st.subheader("🧠 Prep Strategy & Panel Difficulty")
                    st.write(report.interview_section.difficulty_and_tips)
                    st.write("---")
                    
                    st.subheader("⏳ Granular Interview Pipeline Intercept")
                    # Loops through the new structured objects and prints them inside boxed containers
                    for i, step in enumerate(report.interview_section.detailed_stages, 1):
                        with st.container(border=True):
                            head_col, dur_col = st.columns(2)
                            with head_col:
                                st.markdown(f"### {i}. {step.stage_name}")
                            with dur_col:
                                st.markdown(f"⏱️ **Duration:** `{step.duration}`")
                            
                            # Joins the list of focus areas into a clean string separated by dots
                            st.markdown("**🎯 Focus Areas Core Evaluation:** " + " • ".join([f"`{f}`" for f in step.focus_areas]))
                            st.write(step.deep_description)
                    st.write("---")

                    st.subheader("❓ Real-World Interview Questions Captured")
                    for q in report.interview_section.common_questions:
                        st.markdown(f"💬 *\"{q}\"*")
                        
            except Exception as e:
                st.error(f"Failed to generate intelligence data: {e}")
else:
    st.info("👈 Use the left sidebar panel to input your target job search details and run the script.")