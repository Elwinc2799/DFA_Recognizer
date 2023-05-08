# app.py
from flask import Flask, render_template, request, redirect, url_for
import DFA_Recognizer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['text_file']
        if uploaded_file:
            text = uploaded_file.read().decode('utf-8')
            patterns = request.form['patterns'].split(',')
            # Process the text and patterns using your DFA_Recognizer functions
            results = DFA_Recognizer.process_text(text, patterns)
            return render_template('results.html', results=results)
        else:
            return "No file uploaded"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
