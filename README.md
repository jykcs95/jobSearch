# 💼 AI Career Intelligence Platform

A centralized web application dashboard that conducts instant deep-dive research into company positions. It replaces repetitive manual lookups across Glassdoor, Levels.fyi, and tech forums by delivering structured, localized data reports in a single interface.

Built using **Python**, **Streamlit**, and the structured data capabilities of the **Google Gemini 2.5 API**.

---

## ✨ Features

- **Centralized Console View:** Input a target Company, Job Title, and Location to get a comprehensive report in under 10 seconds.
- **Divergent Salary Metrics:** Automatically contrasts **Local Market Pay** side-by-side with **National Market Baselines** (Defaults to Chicago if no location is provided).
- **Employee Sentiment Analysis:** Displays calculated Glassdoor numeric scores (1.0 to 5.0) along with categorized, bulleted pros and cons.
- **Granular Interview Intercept:** Maps out individual interview pipeline cards including the stage name, typical duration, focus metrics, and panel expectations.
- **Optimized UI Design:** Out-of-the-box dark mode styling with global font overrides and suppressed framework helper labels.

---

## 📁 Repository Directory Structure

```text
gemini-app/
├── .env                  # Private API Key (Git-ignored)
├── requirements.txt      # Project Package Dependencies
├── gemini_service.py     # Data Schemas & Gemini Client Call
└── jobSearch.py         # Streamlit Web Application Interface
```

---

## 🛠️ Step-by-Step Installation

### 1. Clone the Repository
Open your terminal window and clone this repository down to your computer:
```bash
git clone https://github.com
cd your-repo-name
```

### 2. Install Project Dependencies
Run the package installer to load all necessary libraries specified in the tracking file:
```bash
pip install -r requirements.txt
```

### 3. Configure Your Environment Secrets
Create a file named `.env` in the root folder to house your confidential keys:
```env
GEMINI_API_KEY=your_actual_google_studio_api_key_here
```
> ⚠️ **Security Reminder:** Never commit your `.env` file to your public GitHub profile. Ensure it is actively tracked in your `.gitignore` configuration.

---

## 🚀 Execution Instructions

Launch the visual web framework dashboard by running this command directly from your VS Code terminal window:

```bash
streamlit run jobSearch.py
```

Streamlit will instantly spin up a local development server and automatically open a new tab session inside your web browser at `http://localhost:8501`.

---

## 🧰 Technical Infrastructure

- **Frontend Interface:** Streamlit (UI Framework)
- **AI Core Framework:** Google GenAI Python SDK (`gemini-2.5-flash`)
- **Data Blueprint Validation:** Pydantic v2
- **Secrets Management:** Python-Dotenv
