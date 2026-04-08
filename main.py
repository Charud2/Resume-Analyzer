import re

# Step 1: Read resume file
with open("sample_resume.txt","r") as file:
    resume_text = file.read().lower()

# Step 2: Define skills
skills_list = ["python", "excel", "sql", "power bi", "tableau"]

# Step 3: Find skills in resume
found_skills = []

for skill in skills_list:
    if skill in resume_text:
        found_skills.append(skill)

# Step 4: Find missing skills
missing_skills = []

for skill in skills_list:
    if skill not in found_skills:
        missing_skills.append(skill)

# Step 5: Output 
print("Skills found in resume:", found_skills)
print("Missing skills:", missing_skills)

# Step 6: Recommendation
if len(missing_skills) > 0:
    print("\nRecommendation: Learn these skills to improve your chances for Data Analyst roles.")
