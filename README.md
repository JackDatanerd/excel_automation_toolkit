Excel Automation Toolkit

Automates repetitive Excel data cleaning and merging workflows for HR, Finance, and Operations teams — saving time and reducing human error.

📌 Overview

Many teams spend hours every month manually cleaning spreadsheets — trimming spaces, standardizing columns, merging files, removing duplicates, and formatting reports.
This toolkit automates that entire workflow using Python + Pandas, producing clean and analysis-ready outputs in seconds.

🚀 Key Features
Feature	Description
Bulk Excel merging	Automatically combines multiple .xlsx files into one dataset
Data cleaning	Trims text, standardizes column names, removes duplicates
Date formatting	Converts messy date fields into proper date format
Automated output	Saves clean, unified report to a data_cleaned/ folder
Reusable workflow	Works for monthly HR logs, finance summaries, sales sheets, etc.
🛠️ Tech Stack

Python

Pandas (data wrangling)

OpenPyXL (writing Excel files)

Glob + OS (file automation)

📂 Project Structure
excel_automation_toolkit/
│
├─ data_raw/                 # Drop messy Excel files here
├─ data_cleaned/             # Cleaned + merged output goes here
├─ reports/                  # (Optional) summaries or pivots
│
├─ automation_toolkit.py     # Main automation script
├─ requirements.txt          # Dependencies
└─ README.md                 # Documentation

▶️ How to Use

Place all raw Excel files in:

data_raw/


Run the script:

python automation_toolkit.py


The cleaned and combined output will appear in:

data_cleaned/cleaned_master.xlsx

📈 Example Use Cases
Department	Task Automated	Time Saved/Month
HR	Consolidating attendance logs	4–6 hours
Finance	Monthly expense sheet cleanup	5–12 hours
Sales	Regional sales performance merging	3–8 hours
🔧 Future Enhancements (Roadmap)

Add UI trigger button directly inside Excel (via xlwings)

Auto-generate pivot summaries & charts

Optional export to Power BI or Streamlit dashboard

Author

Jack — Data Engineer / Analyst | Automation • Analytics • Insight Systems
GitHub → @JackDatanerd
