# Data Analysis Tool

This project is a Python-based tool that accepts a CSV/Excel file upload, performs basic data cleaning, generates meaningful statistical analysis and visualizations, and allows users to interact with the data, generate a summary report, and export the cleaned data.

## Key Features

- **Data Upload & Cleaning:**
  - Accept a CSV/Excel file upload.
  - Remove duplicates and handle missing values (impute with mean/median, or remove rows).
  - Detect text-based numbers and convert them into numeric values.

- **Basic Data Analysis:**
  - Generate basic statistics for the dataset (mean, median, mode, standard deviation).
  - Provide a report summarizing the number of missing values, duplicate entries removed, and any data transformations applied.

- **Data Visualization:**
  - Automatically generate appropriate charts based on data type.
  - Allow users to customize chart labels, titles, and other features.

- **Export Functionality:**
  - Allow users to download the cleaned data in CSV/Excel format.
  - Generate a PDF/Excel report summarizing the data cleaning process and analysis results.

- **User Interaction:**
  - Provide a simple interactive dashboard for viewing the data, statistics, and visualizations.
  - Allow for real-time data processing if users upload new data files.

## Technologies

- Python
- Pandas
- Matplotlib/Plotly
- Flask
- word2number

## Setup

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python run.py`.

## Project Structure

data_analysis_tool/  
├── app/  
│ ├── static/  
│ │ ├── css/  
│ │ │ └── style.css  
│ │ ├── js/  
│ │ │ └── main.js  
│ │ └── uploads/  
│ ├── templates/  
│ │ └── index.html  
│ ├── utils/  
│ │ ├── data_cleaner.py  
│ │ ├── visualizations.py  
│ │ └── text_to_number.py  
│ ├── init.py  
│ └── routes.py  
├── requirements.txt  
├── .gitignore  
├── README.md  
├── run.py  
├── tests/  
│ └── test_data_cleaner.py