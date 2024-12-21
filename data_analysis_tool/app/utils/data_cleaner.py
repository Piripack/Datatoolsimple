import pandas as pd
import numpy as np
from word2number import w2n

def clean_data(file_path):
    # Read the data
    df = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values (impute with mean for numerical columns)
    for column in df.select_dtypes(include=[np.number]).columns:
        df[column].fillna(df[column].mean(), inplace=True)

    # Handle missing values (impute with mode for categorical columns)
    for column in df.select_dtypes(include=[object]).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)

    # Convert text-based numbers to numeric values
    df = df.applymap(lambda x: w2n.word_to_num(x) if isinstance(x, str) and x.replace(' ', '').isalpha() else x)

    return df