import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Data.txt")

# Convert to numeric, coercing any remaining non-numeric values to NaN
df['salary_min'] = pd.to_numeric(df['salary_min'], errors='coerce')
df['salary_max'] = pd.to_numeric(df['salary_max'], errors='coerce')

df_clean_salary = df.dropna(subset=['salary_min', 'salary_max']).copy()

# Calculate the midpoint salary for the clean salary DataFrame
df_clean_salary['midpoint_salary'] = (df_clean_salary['salary_min'] + df_clean_salary['salary_max']) / 2


# Split the location into City and State/Country
df[['city', 'state']] = df['location'].str.split(', ', expand=True)

# For 'Remote' jobs, handle the state/city
df['city'] = df['city'].replace('Remote', 'Remote')
df['state'] = df['state'].fillna('N/A') # Fill NaN in state column for 'Remote'


# c. Extract Experience Level
def categorize_experience(title):
    # ... (function body as defined above)
    title = title.lower()
    if any(keyword in title for keyword in ['principal', 'lead', 'sr.', 'senior', 'architect']):
        return 'Senior/Lead'
    elif any(keyword in title for keyword in ['jr.', 'junior', 'entry level', 'associate', 'devops associate']):
        return 'Junior/Entry'
    elif any(keyword in title for keyword in ['intern', "internship"]):
        return 'Intern'
    else:
        return 'Mid-Level'

df['experience_level'] = df['title'].apply(categorize_experience)
