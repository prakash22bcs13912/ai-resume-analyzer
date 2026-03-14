# Day 3 — Environment Setup ⚙️

## System Information
- OS: macOS
- Python: 3.10+
- Editor: Jupyter Notebook

## Step 1 — Install Python
Downloaded Python from https://python.org/downloads
Verified installation:
```bash
python3 --version
```

## Step 2 — Install Jupyter Notebook
```bash
pip3 install jupyter notebook
```
Launch Jupyter:
```bash
jupyter notebook
```

## Step 3 — Install Project Libraries
```bash
pip3 install spacy pandas numpy matplotlib scikit-learn
pip3 install streamlit pdfplumber
python3 -m spacy download en_core_web_sm
```

## Step 4 — Verify Installations
```python
import spacy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import streamlit

print("spaCy:", spacy.__version__)
print("Pandas:", pd.__version__)
print("NumPy:", np.__version__)
print("Scikit-learn:", sklearn.__version__)
print("✅ All libraries installed successfully!")
```

## Step 5 — GitHub Setup
```bash
# Configure git
git config --global user.name "Jayaprakash"
git config --global user.email "your@email.com"

# Clone repo
git clone https://github.com/prakash22bcs13912/ai-resume-analyzer
cd ai-resume-analyzer
```

## Step 6 — Project Folder Structure
```
ai-resume-analyzer/
├── day1_project_planning.md
├── day2_dataset_collection.md
├── day3_environment_setup.md
├── day4_preprocessing.ipynb
├── day5_cleaning.ipynb
├── day6_feature_extraction.ipynb
├── day8_model_building.ipynb
├── day9_model_evaluation.ipynb
├── day10_nlp_skill_extraction.py
├── day11_resume_scoring.py
├── day12_recommendations.py
├── day13_app.py
├── requirements.txt
└── README.md
```

## ✅ Environment Ready!
All tools installed and GitHub repo connected.
Ready to start coding from Day 4!
