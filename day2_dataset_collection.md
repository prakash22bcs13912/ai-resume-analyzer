# Day 2 — Dataset Collection 📦

## Dataset Used
**Resume Dataset from Kaggle**
- Source: https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset
- Format: CSV
- Size: 2484 resumes
- Categories: 25 job categories

## Dataset Columns
| Column | Description |
|--------|-------------|
| Resume_str | Raw resume text |
| Category | Job category label |

## Job Categories in Dataset
- Data Science
- Web Designing
- HR
- Advocate
- Arts
- Mechanical Engineer
- Sales
- Health and Fitness
- Civil Engineer
- Java Developer
- Business Analyst
- SAP Developer
- Automation Testing
- Electrical Engineering
- Operations Manager
- Python Developer
- DevOps Engineer
- Network Security Engineer
- PMO
- Database Administrator
- Hadoop
- ETL Developer
- DotNet Developer
- Blockchain
- Testing

## Steps Taken
1. Created Kaggle account
2. Downloaded resume dataset (resume.csv)
3. Loaded dataset using Pandas
4. Explored shape, columns, and sample rows
5. Checked for missing values
6. Saved raw data for preprocessing in Day 4

## Key Findings
- Total resumes: 2484
- Total categories: 25
- No major missing values found
- Resume text length varies from 200 to 2000 words

## Code to Load Dataset
```python
import pandas as pd

df = pd.read_csv("resume.csv")
print(df.shape)
print(df.columns)
print(df.head())
print(df["Category"].value_counts())
```
