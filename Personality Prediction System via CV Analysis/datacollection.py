import pandas as pd

# Read in the resume data
resume_df = pd.read_csv('resume_data.csv')

# Read in the cover letter data
cover_letter_df = pd.read_csv('cover_letter_data.csv')

# Merge the resume and cover letter data into one dataset
data_df = pd.merge(resume_df, cover_letter_df, on='candidate_id')
