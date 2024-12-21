from flask import Blueprint, render_template, request, redirect, url_for
from app.utils import data_cleaner, visualizations, text_to_number
import pandas as pd
import os

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'app/static/uploads'
main.config = {'UPLOAD_FOLDER': UPLOAD_FOLDER}


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('main.index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('main.index'))

    if file:
        filepath = os.path.join(main.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process the file
        df = pd.read_csv(filepath)
        cleaned_df = data_cleaner.clean_data(df)
        visualizations.generate_visualizations(cleaned_df)

        return render_template('index.html', tables=[cleaned_df.to_html(classes='data', header="true")])

    return redirect(url_for('main.index'))