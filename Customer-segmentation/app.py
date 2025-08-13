from flask import Flask, render_template, request
import pandas as pd
from kmeans_model import perform_kmeans

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            k = int(request.form['clusters'])
            file = request.files['file']
            if not file:
                return "No file uploaded", 400

            # Read CSV file
            data = pd.read_csv(file)

            # Select first 2 numeric columns
            selected_columns = data.select_dtypes(include=['float64', 'int64']).iloc[:, :2]

            # Drop rows with missing values (NaN)
            selected_columns = selected_columns.dropna()

            # Run KMeans
            result = perform_kmeans(selected_columns.copy(), k)

            return render_template('result.html', table=result.to_html(classes='data'))

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
