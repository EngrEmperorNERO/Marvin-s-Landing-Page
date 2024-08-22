from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# General Settings of the website
PAGE_TITLE = "Personal Landing Website | Marvin Baesa"
PAGE_ICON = ":wave:"
NAME = "Marvin Baesa"
DESCRIPTION = """
A dedicated and results-driven data analyst with more than four years of experience in the field. 
My passion lies in unlocking valuable insights from complex data sets and using them to drive informed decision-making. 
With a strong background in data analysis and visualization, I specialize in data cleaning, transformation, visualization, data modelling / data mapping, data integration, data pipelines, ETL's and storytelling, as well as report generation and automation. 
I also have working knowledge with tools such as Power BI, Salesforce, Python, SQL, and advanced working knowledge in Excel, databases, tableau and MS Access. 
If you're looking for a data analyst who can turn raw data into actionable insights, streamline reporting processes, optimize and improve businesses, I'd love to connect. Let's collaborate and make data-driven decisions that propel your organization forward.
"""
EMAIL = "engr.marvinbaesa01@gmail.com"

SOCIAL_MEDIA = {
    "Github": "https://github.com/EngrEmperorNERO",
    "Facebook": "https://www.facebook.com/profile.php?id=61558530302315"
}


# Ensure set_page_config is called once and at the start
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# Load CSS, PDF, and Profile Pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
#    st.write(EMAIL)

# Experience and Qualifications
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✅ More than 4 years of experience extracting actionable insights from data
    - ✅ Strong hands-on experience and knowledge in Python, SQL, and Excel
    - ✅ Good understanding of statistical principles and their respective applications
    - ✅ Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# Skills
st.write("#")
st.subheader("Relevant Skills: ")
st.write(
    """
    - 👨‍💻 Programming: Python (Pandas, Openpyxl, Numpy, Matplotlib, Selenium, Streamlit, BeautifulSoup)
    - 📊 Data Visualization: Power BI, MS Excel, Google Sheet, and Tableau
    - 🗃️ Data Processing: Data cleaning, Data transformation, Data wrangling, and Data modeling
    - 💻 Database: MySQL and PostgreSQL
    - 💻 KPI Development
    - 💻 Reports Generation / Automation
    - 💻 Salesforce
    - 💻 Advance Working Knowledge in Spreadsheet(Excel, Google Sheet)
    - 💻 Data Collection (Web Scraping, Automation in Data Entry, API)
    - 💻 Data pipelines development 
    - 💻 Data Mapping
    - 💻 Data Processing (Data transformation, Data Cleaning, Data wrangling)
    - 💻 Data Analysis (Descriptive, Predictive, Diagnostic, Exploratory, Regression)
    """
)

# Work History
st.write("#")
st.subheader("Work History")
st.write("---")

#Job 1
st.write("**Data Analyst | E - Commerce**")
st.write("August 2023 - June 2024")
st.write(
    """
    - ▶️ Collect and clean data from various sources
    - ▶️ Identify and analyze trends, patterns and anomalies in complex datasets.
    - ▶️ Create and manage interactive dashboards and reports to visualize data-driven insights.
    - ▶️ Create and maintain data models.
    - ▶️ Locate and define new process for improvement.
    - ▶️ Create monthly and ad-hoc reports.
    - ▶️ Analyze and gather business requirements for stakeholders.
    - ▶️ Develop and implement databases, data collection systems, data analytics and other strategies that optimize statistical efficiency and quality.
    - ▶️ Develop automations script for Daily Reporting/Weekly Report.
    - ▶️ Analyze and Organize raw data.
    - ▶️ Perform tailored financial analyses to assist specific projects or initiatives focused on boosting growth and profitability.
    - ▶️ Developed KPI's that supported business growth and informed strategic decision-making.
    - ▶️ Developed and organized Lead Generation Reporting for Marketing Team.
    - ▶️ Develop Dashboard and KPI's for Customer Lifetime Value.
    """
)

#Job 2
st.write("**Data Engineer Banking Industry**")
st.write("February 2023 - August 2023")
st.write(
    """
    - ▶️ Create and maintain optimal data pipeline architecture
    - ▶️ Work with stakeholders including the Executive, Product, and Data and
    - ▶️ Design teams to assist with data-related technical issues and
    - ▶️ Support their data infrastracture needs.
    - ▶️ Design data integrations and data quality framework.
    - ▶️ Create and design ETL Pipelines base on stakeholders requirements
    - ▶️ Combine raw information from different sources
    - ▶️ Develop Analytical tools and programs
    - ▶️ Analyze and organize raw data
    """
)
#Job 3
st.write("**Data Analyst E-commerce | Oregon USA**")
st.write("January 2022 - February 2023")
st.write(
    """
    - ▶️ Work with executive and other business leaders t identify opportunities for improvement.
    - ▶️ Create report for internal teams and/or external clients Collaborate with team members to collect and analyze data.
    - ▶️ Use graphs, infographs and other methods to visualize data Establish KPIs to measure the effectiveness of business decisions Structure large data sets to find usable information.
    - ▶️ Work with a team of analysts and other associates to process information.
    - ▶️ Create presetations and reports based on recommendations and findings.
    - ▶️ Evaluate business needs and objectives.
    - ▶️ Interpret trends and patterns.
    - ▶️ Develop and track KPIs to inform strategic business decisions.
    - ▶️ Clean and combined data from various sources
    - ▶️ Update and manage inventory system.
    - ▶️ Develop financial models to gain insights about Company's financial performance.
    """
)
#Job 4
st.write("**Junior Logictics Analyst / Financial Analyst | Logistics Industry**")
st.write("December 2020 - January 2022")
st.write(
    """
    - ▶️ Created accurate financial reports and cost analysis to communicate financial performance to key stakeholders.
    - ▶️ Collaborate with various departments to develop and maintain detailed financial models for cost analysis, financial modeling, price index maintenance, and strategic planning.
    - ▶️ Created and Automated Process of Cost Analysis.
    - ▶️ Work with a team of analyst and other associates to process information.
    - ▶️ Create presentations and reports based on recommendations and findings.
    """
)
#Job 5
st.write("**Market Research Analyst | Australian Client - Real Estate**")
st.write("June 2020 - December 2020")
st.write(
    """
    - ▶️ Analyzed comparable properties to assess market value.
    - ▶️ Scraped property listings on various property listing websites.
    - ▶️ Created a dashboard for visualizing and analyzing scraped property listings.
    - ▶️ Collaborated with a team of analyst and associates to process and interpret data.
    - ▶️ Developed presentations and reports base on recommendations and findings.
    - ▶️ Evaluated business needs and objectives, prividing actionable insights.
    - ▶️ Interpreted market trends and patterns to inform strategic decisions.
    - ▶️ Assisted in financial analysis and forecasting reelated to property investments.
    - ▶️ Developed report templates using Excel and Google sheets.
    """
)
st.write("---")

# Title
st.subheader("Trainings and Certifications")

# Details (adding a corresponding URL for each certification)
certifications = [
    ("[Google Data Analytics Professional Certificate](https://coursera.org/share/a320863424369ca0b96fc29ca5455e56)", "Google", "October - December 2022"),
    ("[Scrum Foundation Professional Certificate](https://www.credly.com/badges/d109dda7-1d17-4d2f-8afd-84d3804d22c0/public_url)", "CertiProf", "October 25, 2022"),
    ("[Enterprise Design Thinking Practitioner](https://www.credly.com/badges/39ff5031-68f8-49cb-a38d-497437b07dab/public_url)", "IBM", "November 7, 2022"),
    ("[Data Science Foundations Level 1](https://www.credly.com/badges/81292f68-8c1e-4f54-8e48-bac324e04b07/public_url)", "IBM", "November 4, 2022"),
    ("[Data Science Foundations Level 2](https://www.credly.com/badges/6d8b1973-fa5a-4f53-bf5d-49e4e2eccff0/public_url)", "IBM", "November 4, 2022"),
    ("[Business Intelligence Foundation Professional Certification - BIFPC™](https://www.credly.com/badges/b3b66034-a5c9-47a1-ad66-ce9fddfa2431/public_url)", "CertiProf", "November 30, 2022"),
    ("[Modern Big Data Analysis with SQL](https://coursera.org/share/b40aaaa5b2d0386f59326b47c5217115)", "Cloudera", "December 19, 2022"),
    ("[Foundations of Project Management](https://coursera.org/share/0a4843206a1e4abc56ff1231c1809179)", "Google", "December 27, 2022"),
    ("[Agile Project Management](https://coursera.org/share/01b616a7d49017884666620d2522ea8c)", "Google", "March 3, 2023"),
    ("[Oracle SQL Databases](https://coursera.org/share/4e648b3326eb17d24faa91868f47eb7d)", "LearnQuest", "January 17, 2023"),                  
    ("[Python For Data Science](https://www.credly.com/badges/54ea0eb5-b6bd-49db-a43c-d0ffeb078322/public_url)", "IBM", "January 11, 2023"),
    ("[Data Science Tools](https://www.credly.com/badges/1fd2af22-071b-497c-aec6-5808489b9ded/public_url)", "IBM", "November 4, 2022"),
    ("[Big Data Foundations](https://www.credly.com/badges/262f7067-efba-47cc-88c5-5343c2e155c2/public_url)", "IBM", "November 23, 2022"),
    ("[Hadoop Foundations - Level 1](https://www.credly.com/badges/76320916-4c57-4583-900f-5e9b05ea2bd3/public_url)", "IBM", "November 23, 2022"),
    ("Foundations for Big Data Analysis SQL", "Cloudera", "December 19, 2022"),
    ("Engineer Data in Google Cloud", "Google Cloud Pinas", "Novembe 18, 2022"),
    ("Migrate MySQL Data To Cloud SQL Using Database Migration Service", "Google Cloud Pinas", "Novembe 16, 2022"),
    ("BigQuery Basic for Data Analyst", "Google Cloud Pinas", "Novembe 17, 2022"),
    ("Insights from Data with BigQuery", "Google Cloud Pinas", "Novembe 17, 2022"),
    ("Exploring Data with Looker", "Google Cloud Pinas", "Novembe 19, 2022"),
    ("Data Catalog Fundamentals", "Google Cloud Pinas", "Novembe 19, 2022"),
    ("IBM Data Science Practitioner", "IBM", "Novembe 30, 2023")
    
]

# Divide into 2 columns
col1, col2 = st.columns(2)

# Function to display certifications in a column
def display_certs(column, certs):
    for cert in certs:
        column.markdown(f"**{cert[0]}**")  # Clickable text
        column.write(f"{cert[1]}")
        column.write(f"{cert[2]}")
        column.write("")

# Split the certifications into two halves
half = len(certifications) // 2
certs_col1 = certifications[:half]
certs_col2 = certifications[half:]

# Display certifications in respective columns
display_certs(col1, certs_col1)
display_certs(col2, certs_col2)
