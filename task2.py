import pandas as pd

data = {
    "company_id": ["C101", "C102", "C103"],
    "job_role": ["Data Analyst", "Python Developer", "ML Engineer"],
    "skill_threshold": [40, 70, 85]
}

df = pd.DataFrame(data)

print("Total Jobs Posted:", len(df))
print("Average Skill Threshold:", df["skill_threshold"].mean())
